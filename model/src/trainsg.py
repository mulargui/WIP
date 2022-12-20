import sys, os
import sagemaker
import boto3
from sagemaker.tensorflow import TensorFlow

if __name__ == '__main__':

  #filename of the train set
  TRAINSET = '../../data/train.csv'

  sess = sagemaker.Session()

  #role = sagemaker.get_execution_role()
  #role = 'arn:aws:iam::XXXXXXXXXX:role/service-role/AmazonSageMaker-ExecutionRole-YYYYYYYYYY'
  #role = boto3.client('iam').get_role(RoleName='AmazonSageMaker-ExecutionRole-')['Role']['Arn']
  role = boto3.client('iam').list_roles(PathPrefix='AmazonSageMaker-ExecutionRole-')['Roles'][0]['Arn']
  print(role)
  sys.exit(0)

  #create the job, run in a sagemaker instance
  tf_estimator = TensorFlow(entry_point='main.py', 
    role=role,
    instance_count=1, 
    framework_version='2.1.0', 
    py_version='py3',
    script_mode=True,
    source_dir=os.path.dirname(__file__),
    hyperparameters={'epochs': 1},
    #model_dir='model-registry',
    instance_type='ml.m5.xlarge',
    #use_spot_instances=True,        # Use spot instance
    #max_wait=60*15,                 # Max training time + spot waiting time
    max_run=60*10                    # Max training time
  )

  #training dataset, S3 bucket
  bucket = sess.default_bucket() 
  training_input_path  = sess.upload_data(os.path.join(os.path.dirname(__file__), TRAINSET), bucket)

  #run the job
  tf_estimator.fit({'training': training_input_path})

  from sagemaker.serverless.serverless_inference_config import ServerlessInferenceConfig
  
  #configuration
  serverless_config = ServerlessInferenceConfig(
      memory_size_in_mb=1024,
      max_concurrency=1
  )

  endpoint = tf_estimator.deploy(serverless_inference_config=serverless_config)

  print('Done!')
