const constants = require('./envparams.ts');
const {
	S3Client,
	PutObjectCommand,
	CreateBucketCommand,
	PutBucketWebsiteCommand
} = require("@aws-sdk/client-s3");
const {
    APIGatewayClient,
    GetRestApisCommand
} = require("@aws-sdk/client-api-gateway");
const fs = require('graceful-fs');
const path = require('path');
const replace = require('replace-in-file');

// Set the AWS region and secrets
const config = {
	accessKeyId: constants.AWS_ACCESS_KEY_ID, 
	secretAccessKey: constants.AWS_SECRET_ACCESS_KEY, 
	region: constants.AWS_REGION
};

// Set the bucket parameters
const bucketName = "healthylinkx";
const directoryToUpload = constants.ROOT + '/ux/src';

// ======= helper functions ==========
// Recursively travels a folder tree
function walkSync(currentDirPath, callback) {
	fs.readdirSync(currentDirPath).forEach(function (name) {
		var filePath = path.join(currentDirPath, name);
		var stat = fs.statSync(filePath);
		if (stat.isFile()) {
			callback(filePath, stat);
		} else if (stat.isDirectory()) {
			walkSync(filePath, callback);
		}
	});
}

// ====== create the S3 bucket and copy files =====
async function UXUpdate() {

	try {
		//we need to set the url of the api in the constants.js file
		//URL of the api
		const apigwclient = new APIGatewayClient(config);
		var data = await apigwclient.send(new GetRestApisCommand({}));
		const endpointid = data.items[0].id;
		console.log("API endpoint: " + endpointid);

		// create contants.js with env values
		fs.copyFileSync(constants.ROOT+'/ux/src/js/constants.template.js', constants.ROOT+'/ux/src/js/constants.js');
		const options = {
			files: constants.ROOT+'/ux/src/js/constants.js',
			from: ['APIID', 'REGION'],
			to: [endpointid, constants.AWS_REGION]
		};
		await replace(options);
		console.log("Success. Constants updated.");

		// Create an S3 client service object
		const AWSs3Client = new S3Client(config);
		
		//copy files
		walkSync(directoryToUpload, async function(filePath, stat) {
			let bucketPath = filePath.substring(directoryToUpload.length+1);
			let params = {Bucket: bucketName, Key: bucketPath, Body: fs.readFileSync(filePath), 
				ContentType: 'text/html', ACL:'public-read'};

			//associate the content type related to the file extension
			switch (path.extname(bucketPath)) {
			case '.css':
				params.ContentType='text/css';
				break;
			case '.otf':
				params.ContentType='font/otf';
				break;
			case '.eot':
				params.ContentType='application/vnd.ms-fontobject';
				break;
			case '.svg':
				params.ContentType='image/svg+xml';
				break;
			case '.ttf':
				params.ContentType='font/ttf';
				break;
			case '.woff':
				params.ContentType='font/woff';
				break;
			case '.html':
				params.ContentType='text/html';
				break;
			}

			await AWSs3Client.send(new PutObjectCommand(params));
			console.log("Success. " + bucketPath + " file copied to bucket " + bucketName);
		});
		
		console.log("URL of the bucket: http://" + bucketName + ".s3-website-" + constants.AWS_REGION + ".amazonaws.com/");
	} catch (err) {
			console.log("Error. ", err);
	}
}

module.exports = UXUpdate;