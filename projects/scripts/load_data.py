# Python script to load raw data into MinIO and create Iceberg tables

# imports
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataSetup").getOrCreate()

# dbt-spark requires a namespace named default for some reason
spark.sql("CREATE DATABASE IF NOT EXISTS default")

# load nyc data into lakehouse
spark.sql("CREATE DATABASE IF NOT EXISTS nyc")

spark.sql("DROP TABLE IF EXISTS nyc.taxis")

taxi_file = "/src/data/nyc-taxi-trips/yellow_tripdata_2021-04.parquet"
taxi_trips_df = spark.read.parquet(taxi_file)
taxi_trips_df.write.saveAsTable("nyc.raw_taxi_trips")

# load jaffle shop data into lakehouse
spark.sql("CREATE DATABASE IF NOT EXISTS jaffle_shop")

spark.sql("DROP TABLE IF EXISTS jaffle_shop.raw_customers")
spark.sql("DROP TABLE IF EXISTS jaffle_shop.raw_orders")
spark.sql("DROP TABLE IF EXISTS jaffle_shop.raw_payments")

customer_columns = ["id", "first_name", "last_name"]
order_columns = ["id", "user_id", "order_date", "status"]
payment_columns = ["id", "order_id", "payment_method", "amount"]

jaffle_shop_customers_df = (spark
                            .read.csv(
                                "/src/data/jaffle-shop/raw_customers.csv", 
                                header=True, 
                                inferSchema=True
                            )
                            .toDF(*customer_columns)
                        )
jaffle_shop_orders_df = (spark
                            .read.csv(
                                "/src/data/jaffle-shop/raw_orders.csv", 
                                header=True, 
                                inferSchema=True
                            )
                            .toDF(*order_columns)
                        )
jaffle_shop_payments_df = (spark
                            .read.csv(
                                "/src/data/jaffle-shop/raw_payments.csv", 
                                header=True, 
                                inferSchema=True
                            )
                            .toDF(*payment_columns)
                        )

jaffle_shop_customers_df.write.saveAsTable("jaffle_shop.raw_customers")
jaffle_shop_orders_df.write.saveAsTable("jaffle_shop.raw_orders")
jaffle_shop_payments_df.write.saveAsTable("jaffle_shop.raw_payments")
