from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

weathers = sc.textFile("file:///Users/sriramganesh/Study/Spark/spark_examples/1800.csv")


def parse_line(line):
    fields = line.split(',')
    station_id = fields[0]
    entry_type = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0/5.0) + 32.0
    return station_id, entry_type, temperature


parsed_lines = weathers.map(parse_line)

min_temperature = parsed_lines.filter(lambda line: "TMAX" in line[1])

min_temperature_station = min_temperature.map(lambda x: (x[0], x[2]))

min_temperature_till_date_station = min_temperature_station.reduceByKey(lambda x, y: max(x, y))

for r in min_temperature_till_date_station.collect():
    print("%s, %s" % (r[0], "{:.2f}F".format(r[1])))