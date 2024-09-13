# AWS SDK for Python - used to interact with AWS services
import boto3

import queries


# Initialize the Redshift Data API client
redshift_data = boto3.client('redshift-data')

# Initialize the AWS Secrets Manager client
secrets_manager = boto3.client('secretsmanager')


# Function which ingests the redshift data in CSV format to S3
def unload(sql_query):
    try:
        # Define parameters for Redshift Serverless
        database = 'rs_source'
        secret_arn = 'arn:aws:secretsmanager:ap-southeast-1:345594577144:secret:dwh_secrets-Y4eRM2' # ARN of the secret which stores DB credentials
        workgroup_name = 'dwh-workgroup'
        
        
        # Execute SQL query using Redshift Data API
        response = redshift_data.execute_statement(
            Database=database,
            SecretArn=secret_arn,
            Sql=sql_query,
            WorkgroupName=workgroup_name
        )
    except Exception as e:
        raise # re-raise(throw) the exception caught
    

# Main function
def lambda_handler(event, context):
    try:
        # 1) UNLOAD query for product table
        unload(queries.product_query)
        
        
        # 2) UNLOAD query for product_category table
        unload(queries.product_category_query)
        
        
        # 3) UNLOAD query for order table
        unload(queries.order_query)
        
        
        # 4) UNLOAD query for customer table
        unload(queries.customer_query)

        return "Success"
    except Exception as e:
        print(f"An error occurred: {e}")
        
        return "Fail"
