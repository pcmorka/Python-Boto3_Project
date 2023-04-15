import boto3 #import boto3 module


# Connecting cloud9 to dynamodb
dynamodb = boto3.resource('dynamodb',
    aws_access_key_id='xxxxxxxxxxxx', # Input your access key id
    aws_secret_access_key='xxxxxxxxxxxxxxxx',) # Input your secret key,
    
table = dynamodb.Table('Fruits') #Fruits are items in table

# Batch writing 15 items to table

with table.batch_writer() as batch:
   
   
   batch.put_item(Item={"tag_no": 1010, "name": "Apple"})
   batch.put_item(Item={"tag_no": 1011, "name": "Orange"})
   batch.put_item(Item={"tag_no": 1012, "name": "Strawberry"})
   batch.put_item(Item={"tag_no": 1013, "name": "Pinnapple"})
   batch.put_item(Item={"tag_no": 1014, "name": "Grape"})
   batch.put_item(Item={"tag_no": 1015, "name": "Watermelon"})
   batch.put_item(Item={"tag_no": 1016, "name":"Avocado"})
   batch.put_item(Item={"tag_no": 1017, "name": "Apple berry"})
   batch.put_item(Item={"tag_no": 1018, "name": "Peach"})
   batch.put_item(Item={"tag_no": 1019, "name": "Cherries"})
   batch.put_item(Item={"tag_no": 1020, "name": "Guavaberry"})
   batch.put_item(Item={"tag_no": 1021, "name": "Eggfruit"})
   batch.put_item(Item={"tag_no": 1022, "name": "Dewberries"})
   batch.put_item(Item={"tag": 1023, "name": "Chokecherry"})
   batch.put_item(Item={"tag-id": 1024, "name": "Pear"})
  
print(batch)