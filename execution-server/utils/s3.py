import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def download_file():
    try:
        dataset_path = f'dataset/{}.py'

        bucket = boto3.resource('s3').Bucket(os.getenv('AWS_BUCKET'))
        bucket.download_file(f'/{}.py', dataset_path)

        return dataset_path

    except Exception as e:
        print(e)
