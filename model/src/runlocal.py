import sagemaker

sess = sagemaker.Session()
role = sagemaker.get_execution_role()

from sagemaker.tensorflow import TensorFlow

tf_estimator = TensorFlow(entry_point='mnist_keras_tf.py', 
                          role=role,
                          instance_count=1, 
                          instance_type='local',
                          framework_version='1.15', 
                          py_version='py3',
                          script_mode=True,
                          hyperparameters={'epochs': 1}
                         )