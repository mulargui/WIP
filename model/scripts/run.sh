#!/usr/bin/env bash

#
# You need to add your AWS credentials before executing this script for SGLOCAL and SG modes
# AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ACCOUNT_ID
# AWS_DEFAULT_REGION, AWS_REGION
#

set +x
export DEBIAN_FRONTEND=noninteractive
# Absolute path to this repo
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/model\/scripts//g')

# what you can do
LOCAL=N
SGLOCAL=N
SG=N

# you can also set the flags using the command line
for var in "$@"
do
	if [ "LOCAL" == "$var" ]; then LOCAL=Y 
	fi
	if [ "SGLOCAL" == "$var" ]; then SGLOCAL=Y 
	fi
	if [ "SG" == "$var" ]; then SG=Y 
	fi
done

#train locally
if [ "${LOCAL}" == "Y" ]; then
	docker run -ti -v $REPOPATH:/repo tensorflow/tensorflow /bin/bash /repo/model/scripts/trainlocal.sh
fi

#train locally using sagemaker
#this part doesn't work, wip
if [ "${SGLOCAL}" == "Y" ]; then
	docker run -ti -v $REPOPATH:/repo \
		-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
		-e AWS_REGION -e AWS_DEFAULT_REGION \
	tensorflow/tensorflow /bin/bash /repo/model/scripts/trainsglocal.sh
fi

#train in sagemaker
if [ "${SG}" == "Y" ]; then
	docker run -ti -v $REPOPATH:/repo \
		-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
		-e AWS_REGION -e AWS_DEFAULT_REGION \
		tensorflow/tensorflow /bin/bash /repo/model/scripts/trainsg.sh
fi
