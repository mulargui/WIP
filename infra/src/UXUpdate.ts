const constants = require('./envparams.ts');

const {
	S3Client,
	HeadBucketCommand,
	PutObjectCommand,
	CreateBucketCommand,
	DeletePublicAccessBlockCommand,
	PutBucketPolicyCommand,
	DeleteObjectCommand,
	DeleteBucketCommand
} = require("@aws-sdk/client-s3");

//const Alexa = require('ask-smapi-sdk');
const fs = require('fs');
const replace = require('replace-in-file');
const AdmZip = require('adm-zip');
const exec = require('await-exec');

// Set the bucket parameters
const bucketName = "healthylinkx";
const directoryToUpload = constants.ROOT + '/alexa/src/skill-package';
const filePath = constants.ROOT + '/alexa/src/';
const fileName = 'healthylinkx.zip';

// ====== updates the Healthylinkx Alexa skill =====
async function UXUpdate() {

	try {
		// search for the healthylinkx skill id
		data = await exec(`ask smapi list-skills-for-vendor`); 
		data = JSON.parse(JSON.stringify(data)); //cleans garbage
		console.log(JSON.stringify(data.stdout));
		console.log(JSON.stringify(data.stdout.skills));
		data.stdout.skills.forEach(function(element) {
			console.log(JSON.stringify(element));
		});
		//console.log('skill name: ' + data.stdout.skills[0].nameByLocale.en-US);
		//console.log('skill id: ' + data.stdout.skills[0].skillId);
		return;

		// create skill.json with lambda endpoints
		fs.copyFileSync(directoryToUpload + '/skill.template.json', directoryToUpload + '/skill.json');
		const options = {
			files: directoryToUpload + '/skill.json',
			from: [/AWS_REGION/g, /AWS_ACCOUNT_ID/g],
			to: [process.env.AWS_REGION, process.env.AWS_ACCOUNT_ID]
		};
		await replace(options);
		console.log("Success. lambda endpoints updated.");

		// create a zip package with the alexa skill
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

			//allow public access to the bucket
			await AWSs3Client.send(new DeletePublicAccessBlockCommand({Bucket: bucketName}));

			PublicBucketPolicy = {
				"Version": "2012-10-17",
				"Statement": [{
        			"Sid": "AllowPublicRead",
        			"Effect": "Allow",
        			"Principal": "*",
    				"Action": "s3:GetObject",
    				"Resource": 'arn:aws:s3:::' + bucketName + '/*'
    			}]
			};
			await AWSs3Client.send(new PutBucketPolicyCommand({
				Policy: JSON.stringify(PublicBucketPolicy),
				Bucket: bucketName
			}));
			console.log("Success. " + bucketName + " bucket made public.");
		}

		//copy the zip file to S3
		let params = {Bucket: bucketName, Key: fileName, Body: fs.readFileSync(filePath + '/' + fileName)};

		await AWSs3Client.send(new PutObjectCommand(params));
		console.log("Success. " + fileName + " file copied to bucket " + bucketName);

		//update the Alexa interface
		await exec(`ask smapi import-skill-package --location https://healthylinkx.s3.amazonaws.com/healthylinkx.zip --skill-id ${constants.SKILLID}`); 
		console.log("Success. Alexa updated.");

		//remove resources created
		await fs.unlinkSync(filePath + '/' + fileName);
		await fs.unlinkSync(directoryToUpload + '/skill.json');
		await AWSs3Client.send(new DeleteObjectCommand({ Bucket: bucketName, Key: fileName})); 
		await AWSs3Client.send(new DeleteBucketCommand({ Bucket: bucketName }));
		console.log("Success. All resources deleted.");
		
	} catch (err) {
		console.log("Error. ", err);
	}
}

module.exports = UXUpdate;