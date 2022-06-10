import boto3
import time, urllib
import json
import pathlib


TARGET_BUCKET1 = 'destination-bucket-jan'
TARGET_BUCKET2 = 'destination-bucket-jan2'

def lambda_handler(event, context):
    # # Get the bucket and object key from the Event
    # event = Json.loads()
    print(event)
    print(event['Records'][0]['eventName'])
    
    if event['Records'][0]['eventName']== 'ObjectRemoved:DeleteMarkerCreated':
        s3_client = boto3.client('s3')
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
        file_extension = pathlib.Path(key).suffix
        print(key)
        print(file_extension)
        if file_extension == '.png':
            s3_client.delete_object(
            Bucket = TARGET_BUCKET1,
            Key = key
            )
        elif file_extension == '.txt':
            s3_client.delete_object(
            Bucket = TARGET_BUCKET2,
            Key = key
            )
    else:
        
        s3_client = boto3.client('s3')
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
        file_extension = pathlib.Path(key).suffix
        print(key)
        print(file_extension)
        if file_extension == '.png':
            s3_client.copy_object(
            Bucket = TARGET_BUCKET1,
            Key = key,
            CopySource= {'Bucket': bucket, 'Key': key}
            )
        elif file_extension == '.txt':
            s3_client.copy_object(
            Bucket = TARGET_BUCKET2,
            Key = key,
            CopySource= {'Bucket': bucket, 'Key': key}
            )
 
    
