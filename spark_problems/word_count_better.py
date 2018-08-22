import re
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("WordCountBetter")
sc = SparkContext(conf=conf)


def normalize(text):
    return re.compile('\W+', re.UNICODE).split(text.lower())


input = sc.textFile("book.txt")
words = input.flatMap(normalize)

wordCounts = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x+y).map(lambda x: (x[1], x[0])).sortByKey(ascending=False).collect()

for line in wordCounts:
    word = line[1]
    count = line[0]

    cleanWord = word.encode('ascii', 'ignore')

    if cleanWord:
        print(cleanWord.decode() + " " + str(count))
