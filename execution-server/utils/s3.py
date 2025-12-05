import os
import boto3
from dotenv import load_dotenv
from schemas.execution import ExecutionRequest

load_dotenv()

s3 = boto3.client("s3")
BUCKET = os.getenv("AWS_BUCKET")

def download_file(request: ExecutionRequest):
    try:
        response = s3.list_objects_v2(
            Bucket=BUCKET,
            Prefix=request.function_id
        )

        file_key = response["Contents"][0]["Key"]
        filename = os.path.basename(file_key)
        save_path = f"usercode/{filename}"

        s3.download_file(BUCKET, file_key, save_path)

        return save_path

    except Exception as e:
        print(f"[download_file] ERROR:", e)
        raise e
