import boto3
import qarnot
from botocore.config import Config

if __name__ == '__main__':

    secret_key = "token"
    connection = qarnot.connection.Connection(client_token=secret_key)

    # List buckets using Qarnot's storage API
    buckets = connection.buckets()
    for bucket in buckets:
        print(bucket.uuid)
    print("you have {} buckets.".format(len(buckets)))