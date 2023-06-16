
{{ config(
  persist_docs={"relation": true, "columns": true},
  file_format="iceberg"
) }}

SELECT *
FROM examples.nyc_taxi_yellow
WHERE pickup_time BETWEEN '2021-01-01' AND '2021-01-02'