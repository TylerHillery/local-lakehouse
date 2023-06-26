<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
-->
# **Local Lakehouse Overview**
This provides a docker compose environment to quickly spin up a Spark, Iceberg REST Catalog, MinIO, dbt and soon more. Great for testing ideas and learning.

**note**: If you don't have docker installed, you can head over to the [Get Docker](https://docs.docker.com/get-docker/)
page for installation instructions.

## **Usage**
Start up the docker compose environment by running the following.
```
docker-compose build
```
```
docker-compose up
```

This opens up the following ports:
- MinIO UI http://localhost:9000 use `admin` for username and `password` for password
- Iceberg REST Catalog http://localhost:8181
- Spark UI http://localhost:4040
- Spark Cluster http://localhost:7077
- Spark Driver UI http://localhost:8080
- Spark Thrift Server http://localhost:10000
- Spark History http://localhost:18080
- Jupyter Notebook http://localhost:8888

I have found the best way to interact with these services is opening up a VS Code dev container by attaching to a running docker container or by using the following UIs specified above. 

To stop everything
```
docker-compose down
```

## **Current Services Integrated**
- [x] Spark
- [x] Iceberg REST Catalog
- [x] MinIO
- [x] dbt
- [x] Trino

## **Feature services I want to Integrate**

### Query Engines
- [ ] DuckDB

### Orchestrators
- [ ] Airflow
- [ ] Dagster

### Data Loaders
- [ ] Meltano
- [ ] Airbyte

### Streaming Data Platform
- [ ] Kafka
- [ ] Redpanda 

### Stream Processors & Streaming Databases
- [ ] Flink
- [ ] bytewax
- [ ] Materialize

### Semantic Layer
- [ ] cube

### Data Viz
- [ ] Metabase
- [ ] Rill Data
- [ ] Evidence
- [ ] Streamlit

## **Resources**
- [Iceberg's REST Catalog: A Spark Demo](https://tabular.io/blog/rest-catalog-docker/)
- [GitHub Repo Tabluar Docker-Spark-Iceberg](https://github.com/tabular-io/docker-spark-iceberg)
- [Iceberg + Spark + Trino + Dagster: modern, open-source data stack demo](https://blog.devgenius.io/modern-data-stack-demo-5d75dcdfba50)
- [GitHub Repo Jaffle Shop DuckDB](https://github.com/dbt-labs/jaffle_shop_duckdb)
- [Using dbt with Tabular](https://tabular.io/blog/dbt/)