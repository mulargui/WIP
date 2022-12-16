%%sh
#train locally using sagemaker
#docker run -ti -v $PWD:/WIP tensorflow/tensorflow /bin/bash /WIP/model/src/trainsglocal.sh

#install packages
pip install -q --upgrade pip
pip install -q --upgrade pandas scikit-learn 'sagemaker[local]'

#AWS region to use
export AWS_DEFAULT_REGION=us-east-1

# Absolute path to this file
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/model\/src//g')

#train locally
python3 $REPOPATH/model/src/trainmodel.py local

ls -la $REPOPATH/model-registry
