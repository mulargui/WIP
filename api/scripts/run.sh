#!/usr/bin/env bash

#
# You need to add your AWS credentials before executing this script for SGLOCAL and SG modes
# AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ACCOUNT_ID
# AWS_DEFAULT_REGION, AWS_REGION
# You also need to add the S3 uri to the model in main.py line8
#

set +x
export DEBIAN_FRONTEND=noninteractive
# Absolute path to this repo
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/model\/scripts//g')

#deploy the model as a sagemaker serverless endpoint
if [ "${SG}" == "Y" ]; then
	docker run -ti -v $REPOPATH:/WIP \
		-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
		-e AWS_REGION -e AWS_DEFAULT_REGION \
		tensorflow/tensorflow /bin/bash /WIP/api/scripts/deployapi.sh
fi
