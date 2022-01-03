from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df = spark.read.json("people.json")

print(df.show())