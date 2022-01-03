from pyspark.sql import SparkSession
from delta.tables import DeltaTable
import shutil

spark = SparkSession.builder \
    .appName("utilities") \
    .master("local[*]") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:1.0.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.sql.sources.parallelPartitionDiscovery.parallelism", "4") \
    .getOrCreate()

# Clear previous run's delta-tables
shutil.rmtree("/tmp/delta-table", ignore_errors=True)

# Create a table
print("########### Create a Parquet table ##############")
data = spark.range(0, 5)
data.write.format("parquet").save("/tmp/delta-table")

# Convert to delta
print("########### Convert to Delta ###########")
DeltaTable.convertToDelta(spark, "parquet.`/tmp/delta-table`")

# Read the table
df = spark.read.format("delta").load("/tmp/delta-table")
df.show()

deltaTable = DeltaTable.forPath(spark, "/tmp/delta-table")
print("######## Vacuum the table ########")
deltaTable.vacuum()

print("######## Describe history for the table ######")
deltaTable.history().show()

# Generate manifest
print("######## Generating manifest ######")
deltaTable.generate("SYMLINK_FORMAT_MANIFEST")

# SQL Vacuum
print("####### SQL Vacuum #######")
spark.sql("VACUUM '%s' RETAIN 169 HOURS" % "/tmp/delta-table").collect()

# SQL describe history
print("####### SQL Describe History ########")
print(spark.sql("DESCRIBE HISTORY delta.`%s`" % ("/tmp/delta-table")).collect())

# cleanup
shutil.rmtree("/tmp/delta-table")
