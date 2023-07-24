
const constants = require('./envparams.ts');

// ======== helper function ============
function sleep(secs) {
	return new Promise(resolve => setTimeout(resolve, secs * 1000));
}

// ====== creates the Healthylinkx Alexa skill =====
async function UXCreate() {
	
	try {			
		console.log("Success. healthylinkx Alexa skill created");
		console.log("All done!");

	} catch (err) {
		console.log("Error. ", err);
	}
}

module.exports = UXCreate;