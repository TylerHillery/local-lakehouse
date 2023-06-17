
{{ config(
  persist_docs={"relation": true, "columns": true}
) }}

SELECT *
FROM nyc.taxi_trips