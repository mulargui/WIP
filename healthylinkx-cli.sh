#!/bin/bash
#echo $PWD
#echo $@
echo "Hi"
(cd infra/src; npm install)
node infra/src/index.ts "$@"