const constants = require('./envparams.ts');
const {
	LexModelsV2Client,
	DeleteBotCommand,
	ListBotsCommand
} = require("@aws-sdk/client-lex-models-v2");
const { 
	IAMClient, 
	DeleteServiceLinkedRoleCommand 
} = require("@aws-sdk/client-iam");

// Set the AWS region and secrets
const config = {
	accessKeyId: constants.AWS_ACCESS_KEY_ID, 
	secretAccessKey: constants.AWS_SECRET_ACCESS_KEY, 
	region: constants.AWS_REGION
};

// ====== delete the chatbot and resources =====
async function UXDelete() {
  
	try {
		const lexclient = new LexModelsV2Client(config);
		
		//find the chatbot by name
		var data = await lexclient.send(new ListBotsCommand({filters: [{name: 'BotName', operator: 'EQ', values: ['healthylinkx-bot']}]}));
		const botid = data.botSummaries[0].botId;

		//delete the chatbot and all the resources attached	
		data = await lexclient.send(new DeleteBotCommand({botId: botid, skipResourceInUseCheck: true}));
		console.log("Success. healthylinkx-bot deleted.");

		//delete the role
		const iamclient = new IAMClient(config);
		data = await iamclient.send(new DeleteServiceLinkedRoleCommand({RoleName: 'AWSServiceRoleForLexBots'}));
		console.log("Success. healthylinkx-bot IAM role deleted.");

	} catch (err) {
		console.log("Error. ", err);
	}
}

module.exports = UXDelete;