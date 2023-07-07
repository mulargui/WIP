const constants = require("./constants.js");
const mysql = require('mysql2/promise');

function SearchDoctors(DoctorName, ZipCode, Gender)
{	
	var speakOutput = `You just triggered a search for doctors with the following values:`;
	speakOutput += Gender ? ` gender = ${Gender}` : ``;
	speakOutput += ZipCode ? ` zipcode = ${ZipCode}` : ``;
	speakOutput += DoctorName ? ` name = ${DoctorName}` : ``;

	return speakOutput;
} 

module.exports = SearchDoctors;