import boto3

dynamodb =boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Fruits')

# Write items to table

with table.batch_writer() as batch:
   
   
   batch.put_item(Item={"tag-id": 1010, "name": "Apple"})
   batch.put_item(Item={"tag-id": 1011, "name": "Orange"})
   batch.put_item(Item={"tag-id": 1012, "name": "Strawberry"})
   batch.put_item(Item={"tag-id": 1013, "name": "Pinnapple"})
   batch.put_item(Item={"tag-id": 1014, "name": "Grape"})
   batch.put_item(Item={"tag-id": 1015, "name": "Watermelon"})
   batch.put_item(Item={"tag-id": 1016, "name":"Avocado"})
   batch.put_item(Item={"tag-id": 1017, "name": "Apple berry"})
   batch.put_item(Item={"tag-id": 1018, "name": "Peach"})
   batch.put_item(Item={"tag-id": 1019, "name": "Cherries"})
   batch.put_item(Item={"tag-id": 1020, "name": "Guavaberry"})
   batch.put_item(Item={"tag-id": 1021, "name": "Eggfruit"})
   batch.put_item(Item={"tag-id": 1022, "name": "Dewberries"})
   batch.put_item(Item={"tag-id": 1023, "name": "Chokecherry"})
   batch.put_item(Item={"tag-id": 1024, "name": "Pear"})
  

print(batch)