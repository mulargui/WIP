#!/bin/bash
echo $PWD
#echo $@
(cd infra/src; npm install)
node infra/src/index.ts "$@"