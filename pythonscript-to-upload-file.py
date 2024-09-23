import requests
import json
def get_presigned_url(api_url, file_name):
    try:
        response = requests.get(f"{api_url}?fileName={file_name}")
        print('*'*10)
        response.raise_for_status()
        data = response.json()
        body_data = json.loads(data['body'])
        print(body_data)
        return body_data['url']  

    except requests.exceptions.HTTPError as err:
        raise SystemExit(f"HTTP error occurred: {err}")
    except Exception as err:
        raise SystemExit(f"An error occurred: {err}")

def upload_file_to_s3(presigned_url, file_path):
    try:
        with open(file_path, 'rb') as file:
            response = requests.put(presigned_url, data=file)
            response.raise_for_status() 
        print(f"File uploaded successfully: {file_path}")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(f"HTTP error occurred: {err}")
    except Exception as err:
        raise SystemExit(f"An error occurred: {err}")

def main():
    api_url = "https://hdjkiuymo7.execute-api.us-east-1.amazonaws.com/dev/upload"  # Replace with your API Gateway Invoke URL
    file_path = "plain.txt"  
    file_name = file_path.split("\")[-1] 
    print(file_name)
    presigned_url = get_presigned_url(api_url, file_name)
    upload_file_to_s3(presigned_url, file_path)

if __name__ == "__main__":
    main()
