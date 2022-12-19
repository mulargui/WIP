import argparse, os
import sagemaker
from sagemaker.tensorflow import TensorFlowModel

if __name__ == '__main__':
    
"""
    #get job arguments from sagemaker env
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    args, _ = parser.parse_known_args()
    model_dir  = args.model_dir
"""
    #sess = sagemaker.Session()
    role = sagemaker.get_execution_role()
    model_url = "s3://sagemaker-us-east-1-867679111813/tensorflow-training-2022-12-17-17-26-10-301/output/model.tar.gz"

    #configuration
    serverless_config = ServerlessInferenceConfig(
        memory_size_in_mb=1024,
        max_concurrency=1
    )

    #endpoint creation
    model = TensorFlowModel(model_data=model_url , role=role)
    model.deploy(serverless_inference_config=serverless_config)

    #remove endpoint
    #predictor.delete_endpoint()