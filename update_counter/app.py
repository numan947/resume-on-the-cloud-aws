import json
import requests
import boto3
import os


counter_table_name = 'portfolio-on-the-cloud-aws-counter-table'
ip_table_name = 'portfolio-on-the-cloud-aws-ip-table'
dynamodb = boto3.resource('dynamodb')
counter_table = dynamodb.Table(counter_table_name)
ip_table = dynamodb.Table(ip_table_name)


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

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    
    # counter_table_name = os.environ['COUNTER_TABLE_NAME']
    # ip_table_name = os.environ['IP_TABLE_NAME']
    
    
    
    
    
    print("Hello World!!")

    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'https://*.shasan.xyz',
            'Access-Control-Allow-Methods': 'POST,GET,OPTIONS'
        },
        "body": json.dumps({
            "Message": "Hello World!",
            "CounterTableName": f"{counter_table_name}",
            "IpTableName": f"{ip_table_name}"
        }),
    }
