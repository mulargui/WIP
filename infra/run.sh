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
export REPOPATH=$(dirname "$SCRIPT" | sed 's/infra\\///')
#export REPOPATH=$(dirname "$SCRIPT")

echo $SCRIPT
echo $REPOPATH
echo $PWD
exit

# check if the image is already built, if not build it
if [ "$(docker images | grep base_image)" == "" ]; then
	docker build --rm=true -t base_image $PWD/docker
fi

# run the query
docker run -ti --rm -v $PWD:/repo \
	-w /repo/ \
	-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
	-e AWS_REGION -e AWS_DEFAULT_REGION \
	base_image python3 /repo/healthylinkx-cli.sh "$@"
	#base_image /bin/bash /repo/healthylinkx-cli.sh "$@"