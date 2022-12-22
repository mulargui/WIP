#!/usr/bin/env bash

#
# NOTE: shell script to build and deploy the model in Sagemaker
# This is a great candidate for a jenkins pipeline/AWS code pipeline
# Very lineal implementation, it can be partially parallelized with more code
#

#set +x
#export DEBIAN_FRONTEND=noninteractive
# Absolute path to this repo
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/infra\/pipeline//g')

#aws cli env variables
. ./awsparams.sh

# step1: build the model
if ! $REPOPATH/model/scripts/run.sh SG; then
    echo 'error building the model' 
    exit -1
fi

# step2: create the endpoint
if ! $REPOPATH/api/scripts/run.sh DEPLOY; then
    echo 'error deploying the model' 
    exit -1
fi

# step3: test the endpoint
if ! $REPOPATH/api/scripts/run.sh TEST; then
    echo 'error testing the endpoint' 
    exit -1
fi
