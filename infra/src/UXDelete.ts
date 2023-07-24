
const constants = require('./envparams.ts');

// ====== deletes the Healthylinkx Alexa skill =====
async function UXDelete() {
  
	try {
		console.log("Success. healthylinkx skill deleted.");

	} catch (err) {
		console.log("Error. ", err);
	}
}

module.exports = UXDelete;