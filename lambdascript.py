import json
import boto3

s3_client = boto3.client('s3',region_name="us-east-1")
bucket_name = 'lekhana18'

def lambda_handler(event, context):
    if 'queryStringParameters' in event and 'fileName' in event['queryStringParameters']:
        object_name = event['queryStringParameters']['fileName']
        
        # Generate the presigned URL
        presigned_url = s3_client.generate_presigned_url('put_object', Params={'Bucket': bucket_name, 'Key': object_name}, ExpiresIn=36)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'url': presigned_url})
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing query string parameters or fileName'})
        }
