import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='Fruits',
    KeySchema=[
        {
            'AttributeName': 'tag_no',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'tag_no',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print("Table status:", table.table_status)


