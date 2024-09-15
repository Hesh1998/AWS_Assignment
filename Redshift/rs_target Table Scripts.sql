-- Create sales Schema
CREATE SCHEMA IF NOT EXISTS sales;

-- stg_address table
CREATE TABLE "sales"."stg_address"(
    "customer_id" VARCHAR NULL,
    "address_type" VARCHAR NULL,
    "address_line" VARCHAR NULL,
    "street" VARCHAR NULL,
    "city" VARCHAR NULL,
    "state_province_name" VARCHAR NULL,
    "postal_code" VARCHAR NULL,
    "country" VARCHAR NULL
) DISTSTYLE AUTO

-- stg_customer table
CREATE TABLE "sales"."stg_customer"(
    "customer_id" VARCHAR NULL,
    "first_name" VARCHAR NULL,
    "middle_name" VARCHAR NULL,
    "last_name" VARCHAR NULL,
    "gender" VARCHAR NULL,
    "phone_number" VARCHAR NULL,
    "phone_number_type" VARCHAR NULL,
    "email_address" VARCHAR NULL
) DISTSTYLE AUTO

-- stg_order table
CREATE TABLE "sales"."stg_order"(
    "order_id" VARCHAR NULL,
    "order_date" VARCHAR NULL,
    "status" VARCHAR NULL,
    "product_id" VARCHAR NULL,
    "qty_ordered" VARCHAR NULL,
    "unit_price" VARCHAR NULL,
    "subtotal" VARCHAR NULL,
    "customer_id" VARCHAR NULL
) DISTSTYLE AUTO

-- stg_category table
CREATE TABLE "sales"."stg_category"(
    "category_id" VARCHAR NULL,
    "category" VARCHAR NULL
) DISTSTYLE AUTO

-- stg_product table
CREATE TABLE "sales"."stg_product"(
    "product_id" VARCHAR NULL,
    "product" VARCHAR NULL,
    "unit_price" VARCHAR NULL,
    "stock_code" VARCHAR NULL,
    "category" VARCHAR NULL
) DISTSTYLE AUTO
