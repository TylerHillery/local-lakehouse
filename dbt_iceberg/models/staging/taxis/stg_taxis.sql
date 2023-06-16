
{{ config(
  persist_docs={"relation": true, "columns": true},
  file_format="iceberg"
) }}

SELECT *
FROM nyc.taxis