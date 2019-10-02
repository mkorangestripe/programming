# Dynamodb table creation example

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Put an item into Dynamodb
table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)

# Get and item from dynamodb
response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)



# Dynamodb, Music table example

# Table creation in AWS console
# Table name: Music
# Primary key...
# Partition key: Artist
# Sort key: SongTitle
# Uncheck default settings
# Uncheck Read and Write capacity
# Set Read and Write capacity units to 1
# Under Secondary indexes, click Add index...
# Primary key...
# Partition key: Artist
# Sort key: Rating
# Add/remove attributes: Items, select item, Action, Edit, add item


# songs.json...
# [
#   {
#     "Artist": "Neko Case",
#     "SongTitle": "Hold on, Hold on",
#     "price": "$1.99",
#     "studio": "unknown",
#     "address": "unknown"
#   },
#   {
#     "Artist": "Neko Case",
#     "SongTitle": "Magpie to the Morning",
#     "price": "$0.99",
#     "studio": "unknown",
#     "address": "unknown"
#   },
#   {
#     "Artist": "Neko Case",
#     "SongTitle": "Deep Red Bells",
#     "price": "$2.99",
#     "studio": "unknown",
#     "address": "unknown"
#   }
# ]


# Upload an item to dynamodb
import boto3
import json

dynamodb = boto3.client('dynamodb')

def upload():
    with open('songs.json', 'r') as songfile:
        songs = json.load(songfile)
    for song in songs:
        response = dynamodb.put_item(
            TableName='Music',
            Item={
                'Artist':{'S':song['Artist']},
                'SongTitle':{'S':song['SongTitle']},
                'price':{'S': song['price']},
                'studio':{'S': song['studio']},
                'address':{'S': song['address']}
            }
        )
        print("UPLOADING ITEM")
        print(response)

upload()


# Get and item from dynamodb
gi_res = dynamodb.get_item(
    TableName='Music',
    Key={
        'Artist':{'S':"Neko Case"},
        'SongTitle':{'S':"Magpie to the Morning"}
    },
    ReturnConsumedCapacity='TOTAL'
)
print(gi_res)
