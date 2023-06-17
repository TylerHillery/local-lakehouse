from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataSetup").getOrCreate()
spark.sql("CREATE DATABASE IF NOT EXISTS default")
spark.sql("CREATE DATABASE IF NOT EXISTS nyc")

spark.sql("DROP TABLE IF EXISTS nyc.taxis")

df = spark.read.parquet("/src/data/yellow_tripdata_2021-04.parquet")
df.write.saveAsTable("nyc.taxi_trips")