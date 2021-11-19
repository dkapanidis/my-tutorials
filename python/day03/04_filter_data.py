from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df = spark.read.json("people.json")

print(df.filter("age > 20").show())
# +---+----+
# |age|name|
# +---+----+
# | 30|Andy|
# +---+----+

print(df.filter('name=="Justin"').show())
# +---+------+
# |age|  name|
# +---+------+
# | 19|Justin|
# +---+------+