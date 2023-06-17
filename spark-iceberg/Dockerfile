# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# syntax=docker/dockerfile:1
FROM python:3.9-bullseye

# Optional version env variables
ENV SPARK_VERSION=3.3.2
ENV SPARK_MAJOR_VERSION=3.3
ENV ICEBERG_VERSION=1.3.0
ENV AWSSDK_VERSION=2.20.18

# Optional path env variables
ENV SPARK_HOME=/opt/spark
ENV BIN_DIR=/usr/bin
ENV DBT_DIR=/src/dbt_iceberg
ENV DATA_DIR=/src/data
ENV NOTEBOOKS_DIR=/src/notebooks
ENV SCRIPTS_DIR=/src/scripts
ENV SPARK_EVENTS_DIR=/tmp/spark-events

# Add iceberg spark runtime jar to IJava classpath
ENV IJAVA_CLASSPATH=/opt/spark/jars/*
ENV PATH="/opt/spark/sbin:/opt/spark/bin:${PATH}"
ENV INSTALL_DIR=/tmp/install

# Create dirs
RUN mkdir -p ${SPARK_HOME} ${MINIO_HOME}/bin \ 
            ${DBT_DIR} ${DATA_DIR} ${NOTEBOOKS_DIR}  ${SCRIPTS_DIR} ${SPARK_EVENTS_DIR} ${INSTALL_DIR} \
            /root/.ipython/profile_default/startup

# install core packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
      sudo \
      curl \
      unzip \
      make \
      openjdk-11-jdk \
      build-essential \
      software-properties-common \
      gcc \
      g++ \
      libsasl2-dev \
		  libsasl2-2\ 
		  libsasl2-modules-gssapi-mit\
      ssh  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR ${INSTALL_DIR}

# Install python deps
COPY conf/requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt 

# Add scala kernel via spylon-kernel
RUN python3 -m spylon_kernel install

# Download and install IJava jupyter kernel
RUN curl https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip -Lo ijava-1.3.0.zip \
  && unzip ijava-1.3.0.zip \
  && python3 install.py --sys-prefix \
  && rm -rf ijava-1.3.0.zip	install.py java

# Download spark
RUN curl https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz -o spark-${SPARK_VERSION}-bin-hadoop3.tgz \
 && tar xvzf spark-${SPARK_VERSION}-bin-hadoop3.tgz --directory /opt/spark --strip-components 1 \
 && rm -rf spark-${SPARK_VERSION}-bin-hadoop3.tgz

# Download iceberg spark runtime
RUN curl https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-${SPARK_MAJOR_VERSION}_2.12/${ICEBERG_VERSION}/iceberg-spark-runtime-${SPARK_MAJOR_VERSION}_2.12-${ICEBERG_VERSION}.jar -Lo /opt/spark/jars/iceberg-spark-runtime-${SPARK_MAJOR_VERSION}_2.12-${ICEBERG_VERSION}.jar 

# Download Java AWS SDK
RUN curl https://repo1.maven.org/maven2/software/amazon/awssdk/bundle/${AWSSDK_VERSION}/bundle-${AWSSDK_VERSION}.jar -Lo /opt/spark/jars/bundle-${AWSSDK_VERSION}.jar 

# Download URL connection client required for S3FileIO
RUN curl https://repo1.maven.org/maven2/software/amazon/awssdk/url-connection-client/${AWSSDK_VERSION}/url-connection-client-${AWSSDK_VERSION}.jar -Lo /opt/spark/jars/url-connection-client-${AWSSDK_VERSION}.jar 

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
 && unzip awscliv2.zip \
 && sudo ./aws/install \
 && rm awscliv2.zip \
 && rm -rf aws/

WORKDIR ${SPARK_HOME}

COPY conf/spark-defaults.conf ${SPARK_HOME}/conf
COPY scripts/entrypoint.sh ${BIN_DIR}
COPY conf/ipython/startup/00-prettytables.py /root/.ipython/profile_default/startup
COPY conf/ipython/startup/README.md /root/.ipython/profile_default/startup
COPY conf/notebook ${BIN_DIR}/notebook
COPY conf/notebook ${BIN_DIR}/pyspark-notebook
COPY conf/.pyiceberg.yaml /root/.pyiceberg.yaml

RUN chmod u+x ${SPARK_HOME}/* \
  && chmod u+x ${SPARK_HOME}/bin/* \
  && chmod u+x ${BIN_DIR}/notebook \
  && chmod u+x ${BIN_DIR}/pyspark-notebook

# Download data
RUN curl https://data.cityofnewyork.us/resource/tg4x-b46p.json > /src/data/nyc_film_permits.json \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-04.parquet -o /src/data/yellow_tripdata_2022-04.parquet \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-03.parquet -o /src/data/yellow_tripdata_2022-03.parquet \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-02.parquet -o /src/data/yellow_tripdata_2022-02.parquet \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet -o /src/data/yellow_tripdata_2022-01.parquet \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-12.parquet -o /src/data/yellow_tripdata_2021-12.parquet \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-11.parquet -o /src/data/yellow_tripdata_2021-11.parquet \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-10.parquet -o /src/data/yellow_tripdata_2021-10.parquet \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-09.parquet -o /src/data/yellow_tripdata_2021-09.parquet \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-08.parquet -o /src/data/yellow_tripdata_2021-08.parquet \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-07.parquet -o /src/data/yellow_tripdata_2021-07.parquet \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-06.parquet -o /src/data/yellow_tripdata_2021-06.parquet \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-05.parquet -o /src/data/yellow_tripdata_2021-05.parquet \
 && curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-04.parquet -o /src/data/yellow_tripdata_2021-04.parquet

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
CMD ["spark-submit /src/scripts/load_data.py", "notebook"]
