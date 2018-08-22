from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("CustomerOrder")
sc = SparkContext(conf=conf)

customer_orders = sc.textFile("customer-orders.csv")


def parse_line(line):
    fields = line.split(",")
    return fields[0], float(fields[2])


total_amount_per_customer = customer_orders.map(parse_line).reduceByKey(lambda x, y: x + y).collect()

for each in total_amount_per_customer:
    print("%s: %s" % (each[0], "{:.2f}".format(each[1])))