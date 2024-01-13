import boto3
import json

session = boto3.session.Session()
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name=session.region_name,
)

"""
Function to run inference with models hosted in Bedrock
"""
def run_inference(prompt:str, 
    model:str="amazon.titan-text-express-v1", 
    temperature:float=0.0, 
    max_tokens:int=1000,
    topP:float=1.0) :

    print ("starting run_inference")
    
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

    #return json.loads(output.get('body').read())).get('results')[0].get('outputText')
 
    return json.loads(output.get("body").read()).get('results')[0].get('outputText')


print(run_inference(prompt = "Hi, how are you?"))