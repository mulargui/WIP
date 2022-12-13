import sagemaker
from sagemaker.tensorflow import TensorFlow

if __name__ == '__main__':
  sess = sagemaker.Session()
  role = sagemaker.get_execution_role()

  #upload the training data to S3
  training_input_path   = sess.upload_data('./data/train.csv', key_prefix='kaggle/training')

  #create the job
  tf_estimator = TensorFlow(entry_point='main.py', 
    role=role,
    instance_count=1, 
    instance_type='local',
    framework_version='2.1.0', 
    py_version='py3',
    script_mode=True,
    model_dir='/opt/ml/model',
    hyperparameters={'epochs': 1}
  )

  """
  tf_estimator = TensorFlow(entry_point='main.py', 
                          role=role,
                          train_instance_count=1, 
                          train_instance_type='ml.p3.2xlarge',
                          framework_version='2.1.0', 
                          py_version='py3',
                          script_mode=True,
                          train_use_spot_instances=True,        # Use spot instance
                          train_max_run=600,                    # Max training time
                          train_max_wait=3600,                  # Max training time + spot waiting time
                          model_dir='/opt/ml/model',
                          hyperparameters={'epochs': 1}
                         )
  """

  #run the job
  local_training_input_path = 'file://data/train.csv'
  tf_estimator.fit({'training': training_input_path})
 