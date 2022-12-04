%%sh
pip -q install sagemaker awscli boto3 tensorflow keras --upgrade 

import sagemaker

sess = sagemaker.Session()
role = sagemaker.get_execution_role()

# Where to save the model
%env SM_MODEL_DIR='../../model-registry'
# Where the dataset is
%env SM_DATASET_DIR='../../data'

from sagemaker.tensorflow import TensorFlow

tf_estimator = TensorFlow(entry_point='mnist_keras_tf.py', 
                          role=role,
                          train_instance_count=1, 
                          train_instance_type='local',
                          framework_version='1.15', 
                          py_version='py3',
                          script_mode=True,
                          hyperparameters={'epochs': 1}
                         )