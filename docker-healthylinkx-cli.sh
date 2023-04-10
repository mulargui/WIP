#check if the image is already built, if not build it
if [ "$(docker images | grep node-ask-cli)" == "" ]; then
	docker build --rm=true -t node-ask-cli $PWD/docker
fi

#similar to healthylinkx-cli.sh but running inside a container to avoid to install node, npm...
docker run -ti --rm -v $PWD:/healthylinkx-ask -v $HOME/.ask:/.ask \
	-w /healthylinkx-ask/ \
	node-ask-cli /bin/bash
