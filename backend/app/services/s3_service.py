import boto3
import os
from dotenv import load_dotenv

from botocore.exceptions import ClientError

load_dotenv()


s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv(
        "AWS_ACCESS_KEY_ID"
    ),
    aws_secret_access_key=os.getenv(
        "AWS_SECRET_ACCESS_KEY"
    ),
    region_name=os.getenv(
        "AWS_REGION"
    )
)


BUCKET_NAME = os.getenv(
    "AWS_BUCKET_NAME"
)



import io

def upload_cv_to_s3(content: bytes, filename: str):
    key = f"uploads/{filename}"

    try:
        s3.upload_fileobj(
            io.BytesIO(content),
            BUCKET_NAME,
            key
        )

        print("✅ Upload başarılı:", key)
        return key

    except ClientError as e:
        print("❌ AWS Hatası:")
        print(e.response)
        raise

def generate_presigned_url(key):

    url = s3.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": BUCKET_NAME,
            "Key": key
        },
        ExpiresIn=3600   # 1 saat
    )

    return url