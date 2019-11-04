import ibm_boto3
from ibm_botocore.client import Config
from ibm_botocore.exceptions import ClientError
from ibm_boto3_config import *
import datetime
import sys
import os

config_vars = ['api_key',
               'service_instance_id',
               'service_endpoint',
               'auth_endpoint']

# Check for config variables.
config_not_set = False
for config_var in config_vars:
    if not eval(config_var):
        config_not_set = True
        print(config_var + ' not set')
if config_not_set:
    sys.exit(1)

cos = ibm_boto3.resource('s3',
                         ibm_api_key_id=api_key,
                         ibm_service_instance_id=service_instance_id,
                         ibm_auth_endpoint=auth_endpoint,
                         config=Config(signature_version='oauth'),
                         endpoint_url=service_endpoint)
cos_client = ibm_boto3.client('s3',
                              ibm_api_key_id=api_key,
                              ibm_service_instance_id=service_instance_id,
                              ibm_auth_endpoint=auth_endpoint,
                              config=Config(signature_version='oauth'),
                              endpoint_url=service_endpoint)

# Checking S3 Connection.
if not cos:
    print("\nUnable to obtain S3 connection")
    sys.exit(1)
else:
    print("\nSuccessfully established S3 connection")



def create_bucket(bucket_name):
    """Create a new bucket."""
    print("\nCreating new bucket: {0}".format(bucket_name))
    cos.Bucket(bucket_name).create(
        CreateBucketConfiguration={
            "LocationConstraint": COS_BUCKET_LOCATION
        }
    )

def create_kp_bucket(bucket_name):
    """Create a new KeyProtect bucket."""
    print("\nCreating new bucket: {0}".format(bucket_name))
    cos.meta.client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            "LocationConstraint": COS_BUCKET_LOCATION},
        IBMServiceInstanceId=service_instance_id,
        IBMSSEKPEncryptionAlgorithm='AES256',
        IBMSSEKPCustomerRootKeyCrn=rootkeycrn
    )

def create_bucket_lifecycle_policy(bucket_name, time_before_archive):
    """Create bucket lifecycle policy."""
    now = datetime.datetime.utcnow()
    archive_date = now + datetime.timedelta(minutes=time_before_archive)
    date_to_archive = archive_date.replace(microsecond=0).isoformat()
    
    lifecycle_configuration = {
        "Rules": [
            {
                "Filter": {
                    "Prefix": ""
                },
                "ID": "jlh-test-policy",
                "Status": "Enabled",
                "Transitions": [
                    {
                        "Date": date_to_archive,
                        "StorageClass": "GLACIER"
                    }
                ]
            }
        ]
    }
    
    print("\nSetting lifecycle policy on the bucket")
    try:
        response = cos.meta.client.put_bucket_lifecycle_configuration(Bucket=bucket_name,
            LifecycleConfiguration=lifecycle_configuration)
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def get_bucket_lifecycle_conf(bucket_name):
    """Get bucket lifecycle configuration."""
    print("\nGetting lifecycle policy on the bucket")
    try:
        response = cos.meta.client.get_bucket_lifecycle_configuration(Bucket=bucket_name)
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def delete_bucket_lifecycle_policy(bucket_name):
    """Delete the bucket lifecycle policy."""
    print("\nDeleting lifecycle policy on the bucket")
    try:
        response = cos.meta.client.delete_bucket_lifecycle(Bucket=bucket_name)
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def create_bucket_protect_policy(bucket_name, retention_period):
    """Create bucket protection policy."""
    print("\nSetting protection policy on the bucket")
    try:
        response = cos.meta.client.put_bucket_protection_configuration(Bucket=bucket_name,
            ProtectionConfiguration={'Status': 'Retention',
            'MinimumRetention': {'Days': retention_period},
            'DefaultRetention': {'Days': retention_period},
            'MaximumRetention': {'Days': retention_period}})
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def get_bucket_protection_conf(bucket_name):
    """Get Bucket protection policy configuration."""
    print("\nGetting protection policy on the bucket")
    try:
        response = cos.meta.client.get_bucket_protection_configuration(Bucket=bucket_name)
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def list_buckets(service_instance_id):
    """List all available buckets in the resource group."""
    print("\nPrinting all buckets in the resource group")
    try:
        response = cos_client.list_buckets(
            IBMServiceInstanceId=service_instance_id
        )
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def list_objects(bucket_name):
    # Listing uploaded objects in a bucket
    print ("\nList of objects in the bucket: " + bucket_name)
    try:
        response = cos_client.list_objects(Bucket=bucket_name)
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def delete_multi_object(bucket_name, file_text, file_text_2nd):
    """Delete multiple objects."""
    print("\n Deleting multiple objects form a bucket")
    try:
        response = cos_client.delete_objects(
            Bucket=bucket_name,
            Delete={
                'Objects': [
                    {
                        'Key': file_text
                    },
                    {
                        'Key': file_text_2nd
                    },
                ]
                #'Quiet': True
        })
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def delete_object(bucket_name, file_text):
    """Delete an object."""
    print("\n Deleting an object from the bucket: " + bucket_name)
    try:
        response = cos_client.delete_object(Bucket=bucket_name, Key=file_text)
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def head_object(bucket_name, file_text):
    """Make a head request on the object"""
    print("\nGetting the metadata for " + file_text)
    try:
        response = cos_client.head_object(
            Bucket=bucket_name,
            Key=file_text
        )
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def get_object(bucket_name, file_text):
    """Make a get request on an object"""
    print("\n Getting the object information")
    try:
        response = cos_client.get_object(
            Bucket=bucket_name,
            Key=file_text
        )
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def restore_object(bucket_name, file_text):
    """Restore the object"""
    print("\nRestore the object")
    try:
        response = cos_client.restore_object(
            Bucket=bucket_name,
            Key=file_text,
            RestoreRequest={
                'Days': 1,
                'GlacierJobParameters': {
                    'Tier': 'Bulk'
                }
           },
           RequestPayer='requester'
        )
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def upload_object(file_name, bucket_name, file_text):
    """Upload a file."""
    if os.path.exists(file_name) == False:
        print(file_name + ' not found')
        sys.exit(1)
    print("\nUploading file " + file_name + " to " + bucket_name.title())
    try:
        response = cos.meta.client.upload_file(file_name, bucket_name, file_text)
        print response
    except Exception as e:
        print(type(e))
        print (e.args)

def copy_object(bucket_name, bucket_name_dest, file_text, file_text_copy):
    """Make a copy of an object."""
    print ("\nMaking a copy of an object")
    copy_source = {
    'Bucket': bucket_name,
    'Key': file_text
    }
    try:
        response = cos.meta.client.copy(
            Bucket = bucket_name_dest,
            Key = file_text_copy,
            CopySource = copy_source)
        print response
    except Exception as e:
        print(type(e))
        print (e.args)