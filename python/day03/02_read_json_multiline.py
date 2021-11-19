from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df = spark.read.option("multiLine", True).json("people_multiline.json")

print(df.show())