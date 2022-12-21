import boto3

if __name__ == '__main__':

    endpoint = 'predict-forest-type'
    payload1 = '''{ 
        "features": { 
            "values": [ 2507.0, 160.0, 8.0,
                0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    ] }}'''
    payload = '''{ 
        "input_1": [ 2507.0, 160.0, 8.0,
            0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    }'''
    
    #runtime = boto3.Session().client('sagemaker-runtime')
    runtime = boto3.Session().client('sagemaker')
  
    # Send request via InvokeEndpoint API
    #response = runtime.invoke_endpoint(EndpointName=endpoint, ContentType='application/json', Body=payload)
    response = runtime.describe_endpoint(EndpointName=endpoint)
    print (response)

    # Unpack response
    #result = json.loads(response['Body'].read().decode())
    #print(result)
