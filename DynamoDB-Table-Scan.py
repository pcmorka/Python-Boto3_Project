import boto3 #import boto3 module


# Connecting cloud9 to dynamodb
dynamodb = boto3.resource('dynamodb',

   aws_access_key_id='xxxxxxxxxxxx', # Input your access key id
    aws_secret_access_key='xxxxxxxxxxxxxxxx',) # Input your secret key,



# Here we are scanning the Fruits Table

table = dynamodb.Table('Fruits') #Fruits are items in table


response = table.scan() #input the scan function


items = response['Items']

for item in items:
    print(item)
