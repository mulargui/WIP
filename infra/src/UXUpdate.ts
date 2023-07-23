const constants = require('./envparams.ts');

const {
	S3Client,
	HeadBucketCommand,
	PutObjectCommand,
	CreateBucketCommand,
	PutBucketWebsiteCommand
} = require("@aws-sdk/client-s3");

const fs = require('fs');
const replace = require('replace-in-file');
const AdmZip = require('adm-zip');

// Set the bucket parameters
const bucketName = "healthylinkx";
const directoryToUpload = constants.ROOT + '/alexa/src/skill-package';
const filePath = constants.ROOT + '/alexa/src/';
const fileName = 'healthylinkx.zip';

// ====== copy files to Alexa =====
async function UXUpdate() {

	//create the S3 bucket and copy files
	try {
		// create skill.json with lambda endpoints
		fs.copyFileSync(directoryToUpload + '/skill.template.json', directoryToUpload + '/skill.json');
		const options = {
			files: directoryToUpload + '/skill.json',
			from: [/AWS_REGION/g, /AWS_ACCOUNT_ID/g],
			to: [process.env.AWS_REGION, process.env.AWS_ACCOUNT_ID]
		};
		await replace(options);
		console.log("Success. lambda endpoints updated.");

		//create a zip package with the alexa skill
		const file = new AdmZip();	
		file.addLocalFile(directoryToUpload + '/skill.json');
		file.addLocalFolder(directoryToUpload + '/interactionModels', 'interactionModels');
		file.writeZip(filePath + '/' + fileName);		

		// Create an S3 client service object
		const AWSs3Client = new S3Client({});
		
		// check the S3  bucket exists
		try {
			await AWSs3Client.send(new HeadBucketCommand({ Bucket: bucketName }));
			console.log("Success. " + bucketName + " exists.");
		}catch(err){
			// Create S3 bucket
			await AWSs3Client.send(new CreateBucketCommand({ Bucket: bucketName}));
			console.log("Success. " + bucketName + " bucket created.");
		}

		//copy the zip file to S3
		let params = {Bucket: bucketName, Key: fileName, Body: fs.readFileSync(filePath + '/' + fileName)};
				//ContentType: 'text/html', ACL:'public-read'};

		await AWSs3Client.send(new PutObjectCommand(params));
		console.log("Success. " + fileName + " file copied to bucket " + bucketName);

		//remove the files created
		await fs.unlinkSync(filePath + '/' + fileName);
		await fs.unlinkSync(directoryToUpload + '/skill.json');
	} catch (err) {
		console.log("Error. ", err);
	}
}

module.exports = UXUpdate;