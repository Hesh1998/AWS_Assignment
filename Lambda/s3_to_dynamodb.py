# AWS SDK for Python - used to interact with AWS services
import boto3

import json


# Initialize the S3 client
s3_client = boto3.client('s3')

# Initialize the dynamo db resource
dynamodb = boto3.resource('dynamodb')


# Function which reads address.json data from the S3 bucket
# and writes to dynamo db table
def lambda_handler(event, context):
    try:
        # Get address data from S3
        bucket = 'input-data-dwh'
        json_file_name = 'dataset/address.json'

        json_object = s3_client.get_object(
            Bucket=bucket,
            Key=json_file_name
        )
        
        address_data_dict = json.loads(json_object['Body'].read())
        
        
        # Write address data to dynamo db table
        address_table = dynamodb.Table('Address')

        for i in range(len(address_data_dict['Addresses'])):
            address_table.put_item(Item=address_data_dict['Addresses'][i])
        
        return "Success"
    except Exception as e:
        print(f"An error occurred: {e}")
        
        return "Fail"
