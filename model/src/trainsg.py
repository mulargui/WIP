import sys, os
import boto3
import sagemaker
from sagemaker.tensorflow import TensorFlow

if __name__ == '__main__':

  #filename of the train set
  TRAINSET = '../../data/train.csv'

  #role used in sagemaker
  #role = sagemaker.get_execution_role() #this only works on Sagemaker Studio
  rolelist = boto3.client('iam').list_roles(PathPrefix='/service-role/')['Roles']
  role = [r for r in rolelist if "AmazonSageMaker-ExecutionRole" in r['RoleName']][0]['Arn']
  
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
  sess = sagemaker.Session()
  bucket = sess.default_bucket() 
  training_input_path  = sess.upload_data(os.path.join(os.path.dirname(__file__), TRAINSET), bucket)

  #run the job
  tf_estimator.fit({'training': training_input_path})
 