#train locally
#docker run -ti -v /home/ulargm:/ulargm tensorflow/tensorflow /bin/bash /home/ulargm/WIP/model/src/trainlocal.sh

#install packages
pip install -q --upgrade pip
pip install -q --upgrade pandas scikit-learn

# Absolute path to this file
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/model\/src//g')

#paths to model registry and training data
export SM_MODEL_DIR=$REPOPATH/model-registry
export SM_CHANNEL_TRAINING=$REPOPATH/data

#train locally
python3 $REPOPATH/model/src/main.py