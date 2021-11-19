from pyspark.sql import SparkSession
from pyspark.sql.functions import (col, year, month, dayofmonth)

spark = SparkSession.builder.getOrCreate()
df = spark.read.json("people.json")

# select columns
print(df.select("name", "age").show())
# +-------+
# |   name|
# +-------+
# |Michael|
# |   Andy|
# | Justin|
# +-------+


# rename column
print(df.select(col("name").alias("First Name")).show())
# +----------+
# |First Name|
# +----------+
# |   Michael|
# |      Andy|
# |    Justin|
# +----------+

