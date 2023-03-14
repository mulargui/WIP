#!/bin/bash
pwd
echo $@
(cd infra/src; npm install)
node infra/src/index.ts "$@"