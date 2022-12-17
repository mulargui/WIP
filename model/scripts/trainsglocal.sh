#install packages
pip install -q --upgrade pip
pip install -q --upgrade pandas scikit-learn 'sagemaker[local]' boto3 awscli

#AWS region to use
export AWS_DEFAULT_REGION=us-east-1

# Absolute path to this file
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/model\/scripts//g')

#train locally
python3 $REPOPATH/model/src/trainsglocal.py local

ls -la $REPOPATH/model-registry
