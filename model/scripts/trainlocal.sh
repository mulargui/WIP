#install packages
pip install -q --upgrade pip
pip install -q --upgrade pandas scikit-learn tensorflow

# Absolute path to this file
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/model\/scripts//g')

#paths to model registry and training data
export SM_MODEL_DIR=$REPOPATH/model-registry
export SM_CHANNEL_TRAINING=$REPOPATH/data

#train locally
python3 $REPOPATH/model/src/main.py

ls -la $SM_MODEL_DIR