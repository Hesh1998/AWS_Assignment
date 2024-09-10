-- Products table
CREATE TABLE "public"."product"(
    "product_id" VARCHAR NULL,
    "product" VARCHAR NULL,
    "unit_price" VARCHAR NULL,
    "stock_code" VARCHAR NULL,
    "category" VARCHAR NULL
) DISTSTYLE AUTO

-- ProductCategories table
CREATE TABLE "public"."product_category"(
    "category_id" VARCHAR NULL,
    "category" VARCHAR NULL
) DISTSTYLE AUTO

-- Orders table
CREATE TABLE "public"."order"(
    "order_id" VARCHAR NULL,
    "order_date" VARCHAR NULL,
    "status" VARCHAR NULL,
    "product_id" VARCHAR NULL,
    "qty_ordered" VARCHAR NULL,
    "unit_price" VARCHAR NULL,
    "subtotal" VARCHAR NULL,
    "customer_id" VARCHAR NULL
) DISTSTYLE AUTO

-- Customers table
CREATE TABLE "public"."customer"(
    "customer_id" VARCHAR NULL,
    "first_name" VARCHAR NULL,
    "middle_name" VARCHAR NULL,
    "last_name" VARCHAR NULL,
    "gender" VARCHAR NULL,
    "phone_number" VARCHAR NULL,
    "phone_number_type" VARCHAR NULL,
    "email_address" VARCHAR NULL
) DISTSTYLE AUTO