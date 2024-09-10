-- SP to Truncate and insert S3 data to product_category table
CREATE OR REPLACE PROCEDURE "public"."product_category_i"()
LANGUAGE plpgsql
AS $$
BEGIN
    TRUNCATE TABLE "public"."product_category";

    COPY "public"."product_category"
    FROM 's3://input-data-dwh/dataset/ProductCategories.csv'
    IAM_ROLE 'arn:aws:iam::345594577144:role/Redshift'
    CSV
    IGNOREHEADER 1;
END;
$$;

-- Execute SP to populate product_category table
CALL "public"."product_category_i"();
