import boto3
from botocore.config import Config



ceph_endpoint = "https://storage.qarnot.com"
access_key = "email"  # Qarnot email account
secret_key = "token" # Qarnot Token

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
for bucket in response["Buckets"]:
    print(bucket['Name'])
print("you have {} buckets.".format(len(response["Buckets"])))