import boto3
import json
import os

AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_SESSION_TOKEN=os.environ.get('AWS_SESSION_TOKEN')

session = boto3.session.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN
)

bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name=session.region_name
)

"""
Function to know the models hosted in Bedrock
"""
def list_models() :

    bedrock = boto3.client(
        service_name="bedrock",
        region_name=session.region_name
    )
    print('============================')
    print(AWS_ACCESS_KEY_ID)
    print('============================')
    print(AWS_SECRET_ACCESS_KEY)
    print('============================')
    print(AWS_SESSION_TOKEN)
    print('============================')

     # endpoint_url = 'https://bedrock.us-west-2.amazonaws.com'
    return bedrock.list_foundation_models()['modelSummaries']

"""
Function to run inference with models hosted in Bedrock
"""
def run_inference(prompt:str, 
    model:str="amazon.titan-text-express-v1", 
    temperature:float=0.0, 
    max_tokens:int=1000,
    topP:float=1.0) :

    body = json.dumps({"inputText":prompt,
        "textGenerationConfig": {
            "temperature": temperature,
            "maxTokenCount": max_tokens,
            "topP": topP
        }})

    output = bedrock_runtime.invoke_model(body = body, 
        modelId = model, 
        accept = 'application/json',
        contentType = 'application/json')
 
    return json.loads(output.get("body").read()).get('results')[0].get('outputText')