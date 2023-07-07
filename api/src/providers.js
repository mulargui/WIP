const constants = require("./constants.js");
const mysql = require('mysql2/promise');

function SearchDoctors(DoctorName, ZipCode, Gender)
{	
	var speakOutput = `You just triggered a search for doctors with the following slots `;
	speakOutput += Gender ? `${Gender} ` : ``;
	speakOutput += ZipCode ? `${ZipCode} ` : ``;
	speakOutput += DoctorName ? `${DoctorName} ` : ``;

	return speakOutput;
} 

module.exports = SearchDoctors;