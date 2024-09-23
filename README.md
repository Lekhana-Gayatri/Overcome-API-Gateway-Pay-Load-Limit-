
![Screenshot 2024-09-04 220931](https://github.com/user-attachments/assets/ac6cc063-9e2f-4f98-b74b-d52ffbb7c7b1)

Step 1: Create an S3 Bucket
Step 2: Create a Lambda Function
  * The role should have AmazonS3FullAccess or a more restricted policy that allows the Lambda function to generate pre-signed URLs.
  * In the Environment variables section of the 
    Lambda function, add:
    Key: BUCKET_NAME
    Value: The name of the S3 bucket you created.
Step 3: Create an API Gateway
    * Create Resource Name your resource, e.g., upload, and ensure Enable API Gateway CORS is checked.
    * Create Method Choose GET as the method and click the checkmark Set the Integration type to Lambda Function and select Deploy API
Step 4: Implement the Client-Side Code using        
    pythonscript-to-upload-file.py

You might need to create a mapping template that explicitly maps the query string parameters to the Lambda event object.
Set the content type to application/json, and use the following mapping template:
json

{
    "queryStringParameters": {
        "fileName": "$input.params('fileName')"
    }
}
This template ensures that fileName from the query string is passed correctly to the Lambda function as event['queryStringParameters']['fileName']

ADVANTAGES:
1. Minimizing Backend Load
2. Scalability(Auto-Scaling with S3 and Lambda)
3. Security(Temporary Permissions with Pre-Signed URL)
4.No File Size Limitations(the file size constraints of API Gateway are eliminated)

![Screenshot 2024-09-04 215834](https://github.com/user-attachments/assets/9735ec8e-fb78-4f71-bf27-69058963b519)
