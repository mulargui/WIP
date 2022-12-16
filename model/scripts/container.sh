#!/usr/bin/env bash

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
	docker run -ti -v $REPOPATH:/WIP tensorflow/tensorflow /bin/bash /WIP/model/scripts/trainlocal.sh
fi

#train locally using sagemaker
if [ "${SGLOCAL}" == "Y" ]; then
	docker run -ti -v $REPOPATH:/WIP \
		-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
		-e AWS_REGION -e AWS_DEFAULT_REGION \
	tensorflow/tensorflow /bin/bash /WIP/model/scripts/trainsglocal.sh
fi

#train in sagemaker
if [ "${SG}" == "Y" ]; then
	docker run -ti -v $REPOPATH:/WIP \
		-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
		-e AWS_REGION -e AWS_DEFAULT_REGION \
		tensorflow/tensorflow /bin/bash /WIP/model/scripts/trainmodel.sh
fi
