#!/usr/bin/env bash

#
# NOTE: shell script to build and deploy the API
# This is a great candidate for a jenkins pipeline
# Very lineal implementation, it can be partially parallelized with more code
#

#set +x
#export DEBIAN_FRONTEND=noninteractive
# Absolute path to this repo
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/infra\/pipeline//g')

# step1: build the container to create the model
if ! $REPOPATH/model/docker/container.sh BUILD; then
    echo 'error building the model container' 
    exit -1
fi

# step2: create and train the model
$REPOPATH/model/docker/container.sh RUN
echo $!
wait $!
echo $?

# step3: build the container wiht the api
if ! $REPOPATH/api/docker/container.sh BUILD; then
    echo 'error building the api container' 
    exit -1
fi

# step4: deploy the api
if ! $REPOPATH/api/docker/container.sh RUN; then
    echo 'error starting the server'
    exit -1
fi
echo 'deployment completed'

#step5: test the api
if ! $REPOPATH/api/docker/test.sh; then
    echo 'error testing the api container' 
    exit -1
fi