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
$REPOPATH/model/docker/container.sh BUILD
echo $?
#if ! docker run container/myContainer:latest; then
#  do_stuff
#fi

# step2: create and train the model
$REPOPATH/model/docker/container.sh RUN
wait
echo $?

# step3: build the container wiht the api
$REPOPATH/api/docker/container.sh BUILD
echo $?

# step4: deploy the api
$REPOPATH/api/docker/container.sh RUN
echo $?
echo 'deployment completed'
