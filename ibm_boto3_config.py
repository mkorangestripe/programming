## Prod (creds)
api_key = ''
service_instance_id = ''

## Prod (endpoints)
auth_endpoint = 'https://iam.cloud.ibm.com/oidc/token'
#service_endpoint = 'https://s3.us-east.objectstorage.softlayer.net'
service_endpoint = 'https://s3.us-south.objectstorage.softlayer.net'
#service_endpoint = 'https://s3.eu-gb.objectstorage.softlayer.net'
#service_endpoint = 'https://s3.eu-de.objectstorage.softlayer.net'
#service_endpoint = 'https://s3.jp-tok.objectstorage.softlayer.net'

## Prod (rootcrn for KeyProtect buckets)
## us-east
#rootkeycrn = 'crn:v1:bluemix:public:kms:us-east:xxxxxxxxxx:xxxxxxxxxx:key:xxxxxxxxxx'
## us-south
rootkeycrn = 'crn:v1:bluemix:public:kms:us-south:xxxxxxxxxx:xxxxxxxxxx:key:xxxxxxxxxx'
## eu-gb
#rootkeycrn = 'crn:v1:bluemix:public:kms:eu-gb:xxxxxxxxxx:xxxxxxxxxx:key:xxxxxxxxxx'
## eu-de
#rootkeycrn = 'crn:v1:bluemix:public:kms:eu-de:xxxxxxxxxx:xxxxxxxxxx:key:xxxxxxxxxx'
## jp-tok
#rootkeycrn = 'crn:v1:bluemix:public:kms:jp-tok:xxxxxxxxxx:xxxxxxxxxx:key:xxxxxxxxxx'

## Prod (bucket location)
#COS_BUCKET_LOCATION = 'us-east-test'
#COS_BUCKET_LOCATION = 'us-east-standard'
COS_BUCKET_LOCATION = 'us-south-standard'
#COS_BUCKET_LOCATION = "eu-gb-standard"
#COS_BUCKET_LOCATION = "eu-de-standard"
#COS_BUCKET_LOCATION = "jp-tok-standard"


bucket_name = 'test-bucket-xx-2018-12-10'
#bucket_name_b = 'test-bucket-xx-2018-12-10-b'
#bucket_name = 'kp-test-bucket-xx-2018-12-10'

## These will be used unless set explicitly elsewhere.
## bucket protection config (in days)
retention_period = 1
#retention_period = 0
## bucket lifecycle config (in minutes)
time_before_archive = 5
#time_before_archive = 1

file_name = '10mb.txt'
file_name_2nd = '10mb_2nd.txt'
file_name_3rd = '10mb_3rd.txt'
file_name_4th = '5mb.txt'

file_text = '10mb.txt'
file_text_2nd = '10mb_2nd.txt'
file_text_3rd = '10mb_3rd.txt'
file_text_4th = '5mb.txt'

file_text_copy = '10mb_copy.txt'
