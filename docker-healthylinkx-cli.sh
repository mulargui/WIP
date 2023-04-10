#check if the image is already built, if not build it
if [ "$(docker images | grep node-ask-cli)" == "" ]; then
	docker build --rm=true -t node-ask-cli $PWD/docker
fi

#check we have .ask directory
if [ ! -d $HOME/.ask ]; then
	echo ".ask directory doesn't exist, creating it"
	mkdir $HOME/.ask
fi

#similar to healthylinkx-cli.sh but running inside a container to avoid to install node, npm...
docker run -ti --rm -v $PWD:/healthylinkx-ask -v $HOME/.ask:/root/.ask \
	-w /healthylinkx-ask/ \
	node-ask-cli /bin/bash
