# Import Modules
import boto3

# Clients
session = boto3.Session()
dynamodb = session.client('dynamodb')
s3 = session.client('s3')
sqs = session.client('sqs')
ses = session.client('ses')
ssm = session.client('ssm')
