import boto3
from botocore.config import Config



ceph_endpoint = "https://storage.qarnot.com"  # Replace with your Ceph S3 endpoint
access_key = "robin.royer@qarnot-computing.com"                   # Replace with your Ceph access key
secret_key = "token"

proxy_config = Config(
    proxies={
        'http': 'http://localhost:8080',
        'https': 'http://localhost:8080'
    }
)

s3_client = boto3.client(
    's3',
    endpoint_url=ceph_endpoint,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    config=proxy_config,
    verify=False  # Set to a CA certificate path if needed
)

response = s3_client.list_buckets()
print(response)