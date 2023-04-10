#!/bin/bash

#check we have ASK credentials
if [ ! -e $HOME/.ask/cli_config ]; then
	echo "No ASK credentials, requesting them"
	ask configure --no-browser
fi

#other commands
. sh