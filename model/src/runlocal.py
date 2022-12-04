import sagemaker

sess = sagemaker.Session()
role = sagemaker.get_execution_role()

from sagemaker.tensorflow import TensorFlow

tf_estimator = TensorFlow(entry_point='main.py', 
                          role=role,
                          instance_count=1, 
                          instance_type='local',
                          framework_version='2.0', 
                          py_version='py3',
                          script_mode=True
                        )

#tf_estimator.fit({'training': local_training_input_path, 'validation': local_validation_input_path})
tf_estimator.fit()