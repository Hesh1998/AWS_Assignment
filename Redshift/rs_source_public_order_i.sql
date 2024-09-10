-- SP to Truncate and insert S3 data to order table
CREATE OR REPLACE PROCEDURE "public"."order_i"()
LANGUAGE plpgsql
AS $$
BEGIN
    TRUNCATE TABLE "public"."order";

    COPY "public"."order"
    FROM 's3://input-data-dwh/dataset/Orders.csv'
    IAM_ROLE 'arn:aws:iam::345594577144:role/Redshift'
    CSV
    IGNOREHEADER 1;
END;
$$;

-- Execute SP to populate order table
CALL "public"."order_i"();
