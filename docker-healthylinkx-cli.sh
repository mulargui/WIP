#similar to healthylinkx-cli.sh but running inside a container to avoid to insltall node, npm...
docker run -ti -v $PWD:/healthylinkx-lex -w /healthylinkx-lex/ \
	-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
	-e AWS_REGION -e AWS_DEFAULT_REGION node healthylinkx-cli.sh "$@"
