import json

def lambda_handler(event, context):
    # Example: parse event and return a response
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Hello from the /mcp Lambda!'})
    }
