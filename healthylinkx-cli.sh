#!/bin/bash

#install lambdas and datastore
(cd infra/src; npm install)
node infra/src/index.ts "$@"

#check we have ASK credentials
if [ ! -e $HOME/.ask/cli_config ]; then
	echo "No ASK credentials, requesting them"
	#ask configure --no-browser
fi

#create a new skill
#ask new 

#other commands
/bin/bash
