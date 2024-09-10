-- SP to Truncate and insert S3 data to customer table
CREATE OR REPLACE PROCEDURE "public"."customer_i"()
LANGUAGE plpgsql
AS $$
BEGIN
    TRUNCATE TABLE "public"."customer";

    COPY "public"."customer"
    FROM 's3://input-data-dwh/dataset/Customers.csv'
    IAM_ROLE 'arn:aws:iam::345594577144:role/Redshift' -- ARN of the IAM role (can be found from the console)
    CSV
    IGNOREHEADER 1;
END;
$$;

-- Execute SP to populate customer table
CALL "public"."customer_i"();
