import json
import requests
import boto3
import os
import time


counter_table_name = os.environ['COUNTER_TABLE_NAME']
ip_table_name = os.environ['IP_TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
counter_table = dynamodb.Table(counter_table_name)
ip_table = dynamodb.Table(ip_table_name)

VISITOR_COUNT_KEY = 'VISITOR_COUNT'
TTL_VAL = 30*60 # 30 minutes

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    caller_ip = event['requestContext']['identity']['sourceIp']
    
    # Check if the IP address is already in the table
    response = ip_table.get_item(
        Key={'IpAddress': caller_ip}
    )
    already_exists = response.get('Item') is not None
    
    total_count = 0
    if not already_exists:
        expiresAt = int(time.time()+ TTL_VAL)
        # If the IP address is not in the table, add it
        ip_table.put_item(
            Item={
                'IpAddress': caller_ip,
                'ExpiresAt': expiresAt
                },
            ReturnValues='NONE'
        )
        
        # Increment the counter
        response = counter_table.update_item(
            Key={'PrimaryKey': VISITOR_COUNT_KEY},
            UpdateExpression='ADD CounterValue :inc',
            ExpressionAttributeValues={':inc': 1},
            ReturnValues='ALL_NEW'
        )
        total_count = response['Attributes']['CounterValue']
    elif response['Item']['ExpiresAt'] < int(time.time()):
        # If the IP address is in the table but TTL has expired, update the TTL
        expiresAt = int(time.time()+ TTL_VAL)
        ip_table.update_item(
            Key={'IpAddress': caller_ip},
            UpdateExpression='SET ExpiresAt = :val1',
            ExpressionAttributeValues={':val1': expiresAt},
            ReturnValues='NONE'
        )
        
        # Increment the counter atomically
        response = counter_table.update_item(
            Key={'PrimaryKey': VISITOR_COUNT_KEY},
            UpdateExpression='ADD CounterValue :inc',
            ExpressionAttributeValues={':inc': 1},
            ReturnValues='ALL_NEW'
        )
        total_count = response['Attributes']['CounterValue']
    else:
        response = counter_table.get_item(
            Key={'PrimaryKey': VISITOR_COUNT_KEY}
        )
        total_count = response['Item']['CounterValue']
    
    
    ## Fix the CORS issue
    origin = event['headers']['origin']
    if origin in ['https://smhasan.me', 'https://www.smhasan.me']:
        retOrigin = origin
    else:
        retOrigin = 'https://smhasan.me'
    
    return {
        "statusCode": 200,
        'headers': {
            "Access-Control-Allow-Origin":  f"{retOrigin}",   
			"Access-Control-Allow-Methods": "GET, POST, OPTIONS",
			"Access-Control-Allow-Headers": "Content-Type, X-Amz-Date, Authorization, X-Api-Key, X-Amz-S",
        },
        "body": json.dumps({
            "CounterValue": f"{total_count}",
        }),
    }
