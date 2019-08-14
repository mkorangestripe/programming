# List bucket contents
from boto3.session import Session
access_key='your_access_key'
secret_key='your_secret_key'
session = Session(aws_access_key_id=access_key,
                 aws_secret_access_key=secret_key)
s3 = session.resource('s3')
your_bucket = s3.Bucket('your_bucket')
for s3_file in your_bucket.objects.all():
    print(s3_file.key)


# Upload a file to a bucket
import boto3
f = open('pgbackup-0.1.0-py3-none-any.whl', 'rb')
client = boto3.client('s3')
client.upload_fileobj(f, 'python-db-backups', f.name)


# Encrypt a password with KMS

import boto3
kms = boto3.client('kms')
key_id = 'alias/tempKey'
database_password = 'very-strong-password'
result = kms.encrypt(KeyId=key_id, Plaintext=database_password)

# The CiphertextBlob is the password

# {u'CiphertextBlob': '\x01\x02\x02\x00x\x92D\x8fP\x8e\xa6\xe6\xcf\xee\xf7\xa2\xf0\x9e\xc0\xc1\x94]\x08\xc7\x98\x15\xc5\x9eM\xa2\xdc\xdd\x81\x1a<\x9e\xe0\x01AQ\xc5Fm\xd6\xa3\x0b\xde\xdb{\xe6 2\xdcI\x00\x00\x00r0p\x06\t*\x86H\x86\xf7\r\x01\x07\x06\xa0c0a\x02\x01\x000\\\x06\t*\x86H\x86\xf7\r\x01\x07\x010\x1e\x06\t`\x86H\x01e\x03\x04\x01.0\x11\x04\x0cA\xc3\xbc \x1a\x14F\xd4\xeeyO)\x02\x01\x10\x80/1\x03#\xfe\xef\xfd%L\xdc\xaf-\xd5\x8b \\\xd7+xj\xa9\xf5<\xadbP\xce\x95\xca_\xdd\xeeI\x80\x18\x87\xab\xc6\x1a\x04\x0f\x1c\x1dw:\xd8\x10U',
# u'KeyId': u'arn:aws:kms:us-east-2:193004854402:key/dd86ee04-e563-43fa-ada0-67714bb689bf',
# 'ResponseMetadata': {'HTTPHeaders': {'content-length': '339',
#   'content-type': 'application/x-amz-json-1.1',
#   'x-amzn-requestid': '4875fd8c-ae15-4186-ad81-987953e671f3'},
#  'HTTPStatusCode': 200,
#  'RequestId': '4875fd8c-ae15-4186-ad81-987953e671f3',
#  'RetryAttempts': 0}}

encrypted_password = result['CiphertextBlob']
decrypt_result = kms.decrypt(CiphertextBlob=encrypted_password)

# {u'KeyId': u'arn:aws:kms:us-east-2:193004854402:key/dd86ee04-e563-43fa-ada0-67714bb689bf',
# u'Plaintext': 'very-strong-password',
# 'ResponseMetadata': {'HTTPHeaders': {'content-length': '130',
#   'content-type': 'application/x-amz-json-1.1',
#   'x-amzn-requestid': 'dbc8be3a-2834-437c-b436-77c2848219a6'},
#  'HTTPStatusCode': 200,
#  'RequestId': 'dbc8be3a-2834-437c-b436-77c2848219a6',
#  'RetryAttempts': 0}}


# Send an SNS message
import boto3
sns = boto3.client('sns')
phone_number = '+16125559999'
sns.publish(Message='Hello, test for sns in AWS', PhoneNumber=phone_number)
