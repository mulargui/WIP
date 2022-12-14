import sys, os
import sagemaker
from sagemaker.tensorflow import TensorFlow

if __name__ == '__main__':

  print (os.getcwd())
  
  #run locally in the notebook or use a sagemaker instance
  #if no argument, run on sagemaker by default
  if len(sys.argv) != 2:
    localmode = False
  elif sys.argv[1] == 'local':
    localmode = True
  else:
    localmode = False

  sess = sagemaker.Session()
  role = sagemaker.get_execution_role()

  if localmode:
    #create the job, run localy in the jupyter notebook
    tf_estimator = TensorFlow(entry_point='main.py', 
      role=role,
      instance_count=1, 
      framework_version='2.1.0', 
      py_version='py3',
      script_mode=True,
      model_dir='/tmp/model-registry',
      hyperparameters={'epochs': 1},
      instance_type='local'
    )

    #training dataset, local file
    training_input_path = 'file://./data/train.csv'

  else:
    #create the job, run in a sagemaker instance
    tf_estimator = TensorFlow(entry_point='main.py', 
      role=role,
      instance_count=1, 
      framework_version='2.1.0', 
      py_version='py3',
      script_mode=True,
      model_dir='/tmp/model-registry',
      hyperparameters={'epochs': 1},
      instance_type='ml.p3.2xlarge',
      #use_spot_instances=True,        # Use spot instance
      max_run=60*5                     # Max training time
      #max_wait=60*10                  # Max training time + spot waiting time
    )

    #training dataset, S3 bucket
    bucket = sess.default_bucket() 
    training_input_path  = sess.upload_data('./data/train.csv', bucket)

  #run the job
  tf_estimator.fit({'training': training_input_path})
 