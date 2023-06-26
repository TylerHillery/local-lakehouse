with
rename as (
    select
        VendorID                    as vendor_id,
        tpep_pickup_datetime        as picked_up_at,
        tpep_dropoff_datetime       as dropped_off_at,
        passenger_count,
        trip_distance,
        RatecodeID                  as rate_code_id,
        store_and_fwd_flag,
        PULocationID                as pick_up_location_id,
        DOLocationID                as drop_off_location_id,
        payment_type,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        improvement_surcharge,
        total_amount,
        congestion_surcharge,
        airport_fee
    from
        {{ source('nyc', 'raw_taxi_trips') }}
)

select * from rename