set -x


#remove the API (lambda) from AWS
docker run --rm -w /repo/api/infra -v $(pwd):/repo node:22 npm install
docker run --rm -w /repo/api/infra -v $(pwd):/repo \
	-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
	-e AWS_REGION -e AWS_DEFAULT_REGION -e AWS_SESSION_TOKEN \
    node:22 node delete-api-lambda.js

exit

#remove the front end app from S3 AWS
docker run --rm -w /repo/ux/infra -v $(pwd):/repo node:22 npm install
docker run --rm -w /repo/ux/infra -v $(pwd):/repo \
	-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
	-e AWS_REGION -e AWS_DEFAULT_REGION -e AWS_SESSION_TOKEN \
    node:22 node delete-s3.js