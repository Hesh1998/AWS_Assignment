# List of UNLOAD queries

product_query = "UNLOAD ('SELECT * FROM public.product') TO 's3://sales-data-dwh/dataset/product/' IAM_ROLE 'arn:aws:iam::345594577144:role/Redshift' PARALLEL OFF ALLOWOVERWRITE EXTENSION 'csv' CSV;"

product_category_query = "UNLOAD ('SELECT * FROM public.product_category') TO 's3://sales-data-dwh/dataset/product_category/' IAM_ROLE 'arn:aws:iam::345594577144:role/Redshift' PARALLEL OFF ALLOWOVERWRITE EXTENSION 'csv' CSV;"

order_query = "UNLOAD ('SELECT * FROM public.order') TO 's3://sales-data-dwh/dataset/order/' IAM_ROLE 'arn:aws:iam::345594577144:role/Redshift' PARALLEL OFF ALLOWOVERWRITE EXTENSION 'csv' CSV;"

customer_query = "UNLOAD ('SELECT * FROM public.customer') TO 's3://sales-data-dwh/dataset/customer/' IAM_ROLE 'arn:aws:iam::345594577144:role/Redshift' PARALLEL OFF ALLOWOVERWRITE EXTENSION 'csv' CSV;"
