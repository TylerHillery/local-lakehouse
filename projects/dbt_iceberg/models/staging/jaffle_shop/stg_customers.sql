with 
renamed as (
    select
        id as customer_id,
        first_name,
        last_name
    from
        {{ source('jaffle_shop', 'raw_customers') }}
)

select * from renamed