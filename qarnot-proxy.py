import boto3
import qarnot
from botocore.config import Config


def create_s3_client_and_resource_with_proxy(serviceurl, accesskey, secretkey, proxy_url):
    new_config = Config(
        proxies={
            'http': proxy_url,
            'https': proxy_url
        }
    )

    session = boto3.Session()
    new_s3_resource = session.resource(
        's3',
        endpoint_url=serviceurl,
        aws_access_key_id=accesskey,
        aws_secret_access_key=secretkey,
        config=new_config,
        verify=False  # Set to a CA certificate path if needed
    )

    new_s3_client = session.client(
        's3',
        endpoint_url=serviceurl,
        aws_access_key_id=accesskey,
        aws_secret_access_key=secretkey,
        config=new_config,
        verify=False  # Set to a CA certificate path if needed
    )

    return new_s3_client, new_s3_resource


if __name__ == '__main__':

    secret_key = "token"
    proxy_url = "http://localhost:8080"

    connection = qarnot.connection.Connection(client_token=secret_key)

    # Create a new S3 client with proxy configuration
    s3_client_with_proxy, s3_resource_with_proxy = create_s3_client_and_resource_with_proxy(
        connection.storage,
        connection.user_info.email,
        secret_key,
        proxy_url)

    connection._s3client = s3_client_with_proxy
    connection._s3resource = s3_resource_with_proxy

    # List buckets using Qarnot's storage API
    buckets = connection.buckets()
    for bucket in buckets:
        print(bucket.uuid)
    print("you have {} buckets.".format(len(buckets)))