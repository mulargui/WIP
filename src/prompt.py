import boto3
import json

session = boto3.session.Session()
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name=session.region_name,
)

def run_inference(prompt:str, 
    model:str="amazon.titan-text-express-v1", 
    temperature:float=0.0, 
    max_tokens:int=1000,
    topP:float=1.0) :
    """
    Function to run inference with models hosted in Bedrock
    """
    body = json.dumps({"inputText":prompt,
        "textGenerationConfig": {
            "temperature": temperature,
            "maxTokenCount": max_tokens,
            "topP": topP
        }})

    output = bedrock_runtime.invoke_model(body = body, 
        modelID = model, 
        'application/json',
        'application/json')

    return json.loads(output.get('body'.read())).get('results')[0].get('outputText')


print(run_inference(prompt = "Hi, how are you?"))