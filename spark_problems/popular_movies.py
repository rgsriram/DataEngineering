from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularMovies")
sc = SparkContext(conf=conf)


def load_movie_names():
    movie_names = dict()

    with open("ml-100k/u.item", encoding="ISO-8859-1") as f:
        for line in f:
            fields = line.split('|')
            movie_names[int(fields[0])] = fields[1]

    return movie_names


name_dict = sc.broadcast(load_movie_names())

movies = sc.textFile("ml-100k/u.data")

sorted_movies = movies.map(lambda x: (x.split()[1], 1)).reduceByKey(lambda x, y: x+y).map(lambda x: (x[1], x[0])).sortByKey()

popular_movies = sorted_movies.map(lambda v: (name_dict.value[int(v[1])], v[0])).collect()

for line in popular_movies:
    movie = str(line[0].encode('ascii', 'ignore'))
    count = line[1]
    print("%s, %s" % (movie, count))