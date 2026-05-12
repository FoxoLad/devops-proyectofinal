import boto3
import time

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table_name = "devops-tabla"

print("Creating DynamoDB table...")

table = dynamodb.create_table(
    TableName=table_name,

    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }
    ],

    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        }
    ],

    BillingMode='PAY_PER_REQUEST'
)

print("Waiting for table creation...")

table.wait_until_exists()

print("Inserting item...")

table.put_item(
    Item={
        'id': '1',
        'nombre': 'Proyecto DevOps',
        'status': 'activo'
    }
)

print("Updating item...")

table.update_item(
    Key={
        'id': '1'
    },

    UpdateExpression='SET #s = :new_status',

    ExpressionAttributeNames={
        '#s': 'status'
    },

    ExpressionAttributeValues={
        ':new_status': 'completado'
    }
)

print("Deleting item...")

table.delete_item(
    Key={
        'id': '1'
    }
)

print("DynamoDB operations completed successfully.")
