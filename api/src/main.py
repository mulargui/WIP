import sagemaker
from sagemaker.tensorflow import TensorFlowModel
from sagemaker.serverless.serverless_inference_config import ServerlessInferenceConfig

if __name__ == '__main__':

    role = sagemaker.get_execution_role()
    model_url = "s3://sagemaker-us-east-1-867679111813/tensorflow-training-2022-12-17-17-26-10-301/output/model.tar.gz"

    #configuration
    serverless_config = ServerlessInferenceConfig(
        memory_size_in_mb=1024,
        max_concurrency=1
    )

    #endpoint creation
    model = TensorFlowModel(model_data=model_url , role=role,   framework_version='2.1.0')
    model.deploy(serverless_inference_config=serverless_config)
