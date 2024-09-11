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
        # Get the bucket name
        # and the file path of the json file which was uploaded to trigger lambda function
        bucket = event['Records'][0]['s3']['bucket']['name']
        json_file_name = event['Records'][0]['s3']['object']['key']
        
        
        # Check whether the expected json file was uploaded to S3 bucket
        if(bucket == 'input-data-dwh' and json_file_name == 'dataset/address.json'):
            # Read address data from S3 bucket
            json_object = s3_client.get_object(
                Bucket=bucket,
                Key=json_file_name
            )
            
            address_data_dict = json.loads(json_object['Body'].read())
            
            
            # Write address data to dynamo db table
            address_table = dynamodb.Table('Address')
            
            # Write items seperately to table in dynamo db
            for i in range(len(address_data_dict['Addresses'])):
                address_table.put_item(Item=address_data_dict['Addresses'][i])
            
        return "Success"
    except Exception as e:
        print(f"An error occurred: {e}")
        
        return "Fail"
