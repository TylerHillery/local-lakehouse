# Python script to load raw data into MinIO and create Iceberg tables

# imports
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataSetup").getOrCreate()
# dbt-spark requires a namespace named default for some reason
spark.sql("CREATE DATABASE IF NOT EXISTS default")

# load nyc data into lakehouse
spark.sql("CREATE DATABASE IF NOT EXISTS nyc")

spark.sql("DROP TABLE IF EXISTS nyc.taxis")

taxi_trips_df = spark.read.parquet("/src/data/nyc-taxi-trips/*.parquet")
taxi_trips_df.write.saveAsTable("nyc.raw_taxi_trips")

# load jaffle shop data into lakehouse
spark.sql("CREATE DATABASE IF NOT EXISTS jaffle_shop")

spark.sql("DROP TABLE IF EXISTS jaffle_shop.customers")
spark.sql("DROP TABLE IF EXISTS jaffle_shop.orders")
spark.sql("DROP TABLE IF EXISTS jaffle_shop.payments")

jaffle_shop_customers_df = spark.read.csv("/src/data/jaffle-shop/raw_customers.csv")
jaffle_shop_orders_df = spark.read.csv("/src/data/jaffle-shop/raw_orders.csv")
jaffle_shop_payments_df = spark.read.csv("/src/data/jaffle-shop/raw_payments.csv")

jaffle_shop_customers_df.write.saveAsTable("jaffle_shop.raw_customers")
jaffle_shop_orders_df.write.saveAsTable("jaffle_shop.raw_orders")
jaffle_shop_payments_df.write.saveAsTable("jaffle_shop.payments")

