# AWS SDK for Python - used to interact with AWS services
import boto3

import json
import pandas as pd
from io import StringIO

# Initialize the S3 client
s3_client = boto3.client('s3')

# Initialize the dynamo db resource
dynamodb = boto3.resource('dynamodb')


# Function which reads address data from DynamoDB
# And writes in CSV format to S3 data lake
def lambda_handler(event, context):
    try:
        # Get the table and extract all items
        table = dynamodb.Table('Address')
        response = table.scan()
        items = response['Items']
        
        
        # Creating an empty pandas dataframe to store the address data
        columns = ['CustomerID', 'AddressType', 'AddressLine', 'Street', 'City', 'StateProvinceName', 'PostalCode', 'Country']
        df = pd.DataFrame(columns=columns, dtype=str)
        
        
        # Storing address data in the pandas dataframe
        j = 0
        for i in range(len(items)):
            df.loc[j] = [items[i]['CustomerID'], items[i]['AddressType'], '1', items[i]['Address']['AddressLine1']['Street'], items[i]['Address']['AddressLine1']['City'], items[i]['Address']['AddressLine1']['StateProvinceName'], items[i]['Address']['AddressLine1']['PostalCode'], items[i]['Country']]
            j += 1
            df.loc[j] = [items[i]['CustomerID'], items[i]['AddressType'], '2', items[i]['Address']['AddressLine2']['Street'], items[i]['Address']['AddressLine2']['City'], items[i]['Address']['AddressLine2']['StateProvinceName'], items[i]['Address']['AddressLine2']['PostalCode'], items[i]['Country']]
            j += 1        
        
        
        # Saving the datafrmae to S3
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False, header=False)
        bucket_name = 'sales-data-dwh'
        file_name = 'dataset/address_data.csv'
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())
        
        return "Success"
    except Exception as e:
        print(f"An error occurred: {e}")
        
        return "Fail"
