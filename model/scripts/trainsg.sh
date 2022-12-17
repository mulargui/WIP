#install packages
pip install -q --upgrade pip
pip install -q --upgrade sagemaker

# Absolute path to this file
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/model\/scripts//g')

#train in sagemaker
python3 $REPOPATH/model/src/trainsg.py
