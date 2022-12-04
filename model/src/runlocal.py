import sagemaker

sess = sagemaker.Session()
role = sagemaker.get_execution_role()

from sagemaker.tensorflow import TensorFlow

tf_estimator = TensorFlow(entry_point='main.py', 
                          role=role,
                          instance_count=1, 
                          instance_type='local',
                          framework_version='1.15', 
                          py_version='py3',
                          script_mode=True,
                          hyperparameters={'epochs': 1}
                         )

#local_training_input_path   = 'file://data/training.npz'
#local_validation_input_path = 'file://data/validation.npz'

#tf_estimator.fit({'training': local_training_input_path, 'validation': local_validation_input_path})
tf_estimator.fit()