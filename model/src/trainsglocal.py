import sys, os
import sagemaker
from sagemaker.local import LocalSession
from sagemaker.tensorflow import TensorFlow

if __name__ == '__main__':

  #filename of the train set
  TRAINSET = '../../data/train.csv'
  
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
    source_dir=os.getcwd(),
    hyperparameters={'epochs': 1},
    model_dir=os.path.join(os.getcwd(), '../../model-registry'),
    instance_type='local'
  )

  #training dataset, local file
  training_input_path = 'file://'+os.path.join(os.getcwd(), TRAINSET)
  print (training_input_path)
 
  #run the job
  tf_estimator.fit({'training': training_input_path})
 