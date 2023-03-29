const constants = require("./constants.js");
const mysql = require('mysql2/promise');

var db = await mysql.createPool({
	host:constants.host,
	user:constants.user,
	password:constants.password,
	database:constants.database
});

function SearchDoctors(DoctorName, ZipCode, Gender)
{	
 	//check params
 	if(!ZipCode && !DoctorName && !Gender)
		return {"code": 204, "text": "error: not enought params"};

	//normalize gender
	if (Gender === 'male') Gender = 'M';
	if (Gender === 'm') Gender = 'M';
	if (Gender !== 'M') Gender = 'F';

 	var query = "SELECT NPI,Provider_Full_Name,Provider_Full_Street,Provider_Full_City FROM npidata2 WHERE (";
 	if(DoctorName)
 		query += "(Provider_Last_Name_Legal_Name = '" + DoctorName + "')";
 	if(Gender)
 		if(DoctorName)
 			query += " AND (Provider_Gender_Code = '" + Gender + "')";
 		else
 			query += "(Provider_Gender_Code = '" + Gender + "')";
 	if(ZipCode)
 		if(DoctorName || Gender)
 			query += " AND (Provider_Short_Postal_Code = '"+ ZipCode + "')";
 		else
 			query += "(Provider_Short_Postal_Code = '" + ZipCode + "')";
	query += ") limit 10";

	query = JSON.stringify(db);

	return {"code": 200, "text": query};
/*
	try {
		const [rows,fields] = await db.query(query);
		return {"code": 200, "text": rows};
	} catch(err) {
		return {"code": 500, "text": "error: ${query}  ${err}"};
	}*/
}; 

module.exports = SearchDoctors;