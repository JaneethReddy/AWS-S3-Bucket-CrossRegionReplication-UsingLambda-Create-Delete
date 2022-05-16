import boto3
import time, urllib
import json


TARGET_BUCKET1 = 'destinationbucket-1'
TARGET_BUCKET2 = 'destinationbucket2'
def lambda_handler(event, context):
    # # Get the bucket and object key from the Event
    # event = Json.loads()
    if event['Records'][0]['eventName']== 'ObjectRemoved:Delete':
        s3_client = boto3.client('s3')
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
        s3_client.delete_object(
        Bucket = TARGET_BUCKET1,
        Key = key
        )
        s3_client.delete_object(
        Bucket = TARGET_BUCKET2,
        Key = key
        )
    else:
        s3_client = boto3.client('s3')
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
        s3_client.copy_object(
        Bucket = TARGET_BUCKET1,
        Key = key,
        CopySource= {'Bucket': bucket, 'Key': key}
        )
        s3_client.copy_object(
        Bucket = TARGET_BUCKET2,
        Key = key,
        CopySource= {'Bucket': bucket, 'Key': key}
        )
 
    
