#install packages
pip install -q --upgrade pip
pip install -q --upgrade sagemaker

#AWS region to use
export AWS_DEFAULT_REGION=us-east-1

# Absolute path to this file
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/model\/scripts//g')

#train in sagemaker
python3 $REPOPATH/model/src/trainsg.py
