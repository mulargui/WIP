import sys, os
import sagemaker
from sagemaker.tensorflow import TensorFlow

if __name__ == '__main__':

  #filename of the train set
  TRAINSET = '../../data/train.csv'
  
  #run locally in the notebook or use a sagemaker instance
  #if no argument, run on sagemaker by default
  if len(sys.argv) != 2:
    localmode = False
  elif sys.argv[1] == 'local':
    localmode = True
  else:
    localmode = False
 
  if localmode:
    from sagemaker.local import LocalSession

    sagemaker_session = LocalSession()
    sagemaker_session.config = {'local': {'local_code': True}}
    role = 'ME'

    #create the job, run localy in the jupyter notebook instance
    tf_estimator = TensorFlow(entry_point='main.py', 
      role=role,
      instance_count=1, 
      framework_version='2.1.0', 
      py_version='py3',
      script_mode=True,
      #source_dir=os.getcwd(),
      hyperparameters={'epochs': 1},
      model_dir=os.path.join(os.getcwd(), '../../model-registry'),
      instance_type='local'
    )

    #training dataset, local file
    training_input_path = 'file://'+os.path.join(os.getcwd(), TRAINSET)
    print (training_input_path)

  else:
    sess = sagemaker.Session()
    role = sagemaker.get_execution_role()

    #create the job, run in a sagemaker instance
    tf_estimator = TensorFlow(entry_point='main.py', 
      role=role,
      instance_count=1, 
      framework_version='2.1.0', 
      py_version='py3',
      script_mode=True,
      source_dir=os.getcwd(),
      hyperparameters={'epochs': 1},
      #model_dir='model-registry',
      instance_type='ml.m5.xlarge',
      #use_spot_instances=True,        # Use spot instance
      #max_wait=60*15,                 # Max training time + spot waiting time
      max_run=60*10                    # Max training time
   )

    #training dataset, S3 bucket
    bucket = sess.default_bucket() 
    training_input_path  = sess.upload_data(os.path.join(os.getcwd(), TRAINSET), bucket)

  #run the job
  print ('starting fit')
  tf_estimator.fit({'training': training_input_path})
  print ('ending fit')
 