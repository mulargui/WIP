#!/usr/bin/env bash

#
# NOTE: used to test the container outside k8s
#

set +x
export DEBIAN_FRONTEND=noninteractive
# Absolute path to this repo
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/api\/docker//g')

# what you can do
CLEAR=N
CLEANUP=N
BUILD=N
RUN=N
INTERACTIVE=N

# you can also set the flags using the command line
for var in "$@"
do
	if [ "CLEAR" == "$var" ]; then CLEAR=Y 
	fi
	if [ "CLEANUP" == "$var" ]; then CLEANUP=Y 
	fi
	if [ "BUILD" == "$var" ]; then BUILD=Y 
	fi
	if [ "RUN" == "$var" ]; then RUN=Y 
	fi
	if [ "INTERACTIVE" == "$var" ]; then INTERACTIVE=Y 
	fi
done

# clean up all containers
if [ "${CLEAR}" == "Y" ]; then
	sudo docker stop MODEL-API
	sudo docker kill MODEL-API
	sudo docker rm -f MODEL-API
fi

# clean up all images
if [ "${CLEANUP}" == "Y" ]; then
	$0 CLEAR
	sudo docker rmi -f model-api
fi

# create image
if [ "${BUILD}" == "Y" ]; then
	$0 CLEAR
	$0 CLEANUP
	sudo docker build $REPOPATH --rm=true -t model-api -f $REPOPATH/api/docker/dockerfile
fi

# run the container in the background
if [ "${RUN}" == "Y" ]; then
	sudo docker run -d --name MODEL-API -p 80:80 -v $REPOPATH/data:/data -v $REPOPATH/model-registry:/model-registry model-api
fi

# run the container in the console
if [ "${INTERACTIVE}" == "Y" ]; then
	sudo docker run -ti --name MODEL-API -p 80:80 -v $REPOPATH/api/src:/src2 -v $REPOPATH/data:/data -v $REPOPATH/model-registry:/model-registry model-api /bin/bash
	#sudo docker run -ti --name MODEL-API -p 80:80 -v $REPOPATH/data:/data -v $REPOPATH/model-registry:/model-registry model-api /bin/bash
	#uvicorn src.main:app --host 0.0.0.0 --port 80
fi
