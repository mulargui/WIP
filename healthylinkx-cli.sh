#!/bin/bash

(cd infra/src; npm install)
echo $PWD
node infra/src/index.ts "$@"