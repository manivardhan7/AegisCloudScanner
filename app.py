import json
import boto3
import yara

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))
    s3 = boto3.client('s3')

    try:
        # Extract bucket and key
        record = event['Records'][0]
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print(f"Processing file s3://{bucket}/{key}")

        # Download file from S3 to Lambda's /tmp folder
        local_path = '/tmp/' + key.split('/')[-1]
        s3.download_file(bucket, key, local_path)
        print(f"Downloaded file to {local_path}")

        # Compile YARA rules (use your rules file location)
        rules = yara.compile('/tmp/malicious_rules.yar')

        # Scan the downloaded file
        matches = rules.match(local_path)
        if matches:
            print(f"Malware detected! Matches: {matches}")
        else:
            print("No threat found.")

        return {
            'statusCode': 200,
            'body': f'Scan complete. Matches: {matches}'
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': 'Error scanning file'
        }
