import boto3
import sagemaker
from sagemaker.tensorflow import TensorFlowModel
from sagemaker.serverless.serverless_inference_config import ServerlessInferenceConfig

if __name__ == '__main__':

    #role used in sagemaker
    #role = sagemaker.get_execution_role() #this only works on Sagemaker Studio
    rolelist = boto3.client('iam').list_roles(PathPrefix='/service-role/')['Roles']
    role = [r for r in rolelist if "AmazonSageMaker-ExecutionRole" in r['RoleName']][0]['Arn']

    #temporary
    model_url = "s3://sagemaker-us-east-1-867679111813/tensorflow-training-2022-12-20-22-54-39-411/output/model.tar.gz"

    #configuration
    serverless_config = ServerlessInferenceConfig(
        memory_size_in_mb=1024,
        max_concurrency=1
    )

    #endpoint creation
    model = TensorFlowModel(model_data=model_url, role=role, framework_version='2.1.0')
    model.deploy(serverless_inference_config=serverless_config, endpoint_name='predict-forest-type')
