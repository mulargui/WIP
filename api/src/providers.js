const constants = require("./constants.js");
const mysql = require('mysql2/promise');

var db = mysql.createPool({
	host:constants.host,
	user:constants.user,
	password:constants.password,
	database:constants.database
});

function FormatResult(rows){
    if (rows == null) return 'Sorry, no matching providers were found.';
    if (!rows.length) return 'Sorry, no matching providers were found.';
	
    var output = `These are the doctors we found for you: `;
    for (var i = 0; i < rows.length; i++) {
        if (rows[i].hasOwnProperty(0)) 
            output += ("Name: " + rows[i][0]);
		if (rows[i].hasOwnProperty(1)) 
            output += ("Address: " + rows[i][1]);
		if (rows[i].hasOwnProperty(2)) 
            output += ("City: " + rows[i][2]);
    }
    return output;
}

function SearchDoctors(DoctorName, ZipCode, Gender)
{	
	//check params
 	if(!ZipCode && !DoctorName && !Gender)
		return "Sorry, I need more information to  search for doctors";

	//normalize gender
	if (Gender){
		if (Gender === 'male') Gender = 'M';
		if (Gender === 'm') Gender = 'M';
		if (Gender !== 'M') Gender = 'F';
	}
	var speakOutput = `You just triggered a search for doctors with the following values:`;
	speakOutput += Gender ? ` gender = ${Gender}` : ``;
	speakOutput += ZipCode ? ` zipcode = ${ZipCode}` : ``;
	speakOutput += DoctorName ? ` name = ${DoctorName}` : ``;

	return speakOutput;
} 

module.exports = SearchDoctors;