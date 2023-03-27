const constants = require("./constants.js");
const mysql = require('mysql2/promise');
const axios = require('axios');

function ServerReply (code, event, result){
	
	if (code == 200)
		event.sessionState.intent.state = 'Fulfilled';	
	else
		event.sessionState.intent.state = 'Failed';	

    return {
        sessionState: {
            sessionAttributes: event.sessionState.sessionAttributes,
            dialogAction: {
                type: 'Close'
            },
            intent: event.sessionState.intent
        },
        messages: [{
            contentType: 'PlainText',
            content: 'original event: ' + JSON.stringify(event) + ' #end' +
                'results: ' + JSON.stringify(result) + ' #end'
        }],
        sessionId: event.sessionId,
        requestAttributes: event.requestAttributes
    };
}

function SearchDoctors (event){
    /*return ServerReply (200, event, {"slots":[
        {"attr": Object.keys(event.interpretations[0].intent.slots)[0],
            "value": Object.values(event.interpretations[0].intent.slots)[0].value.interpretedValue},
        {"attr": Object.keys(event.interpretations[0].intent.slots)[1],
            "value": Object.values(event.interpretations[0].intent.slots)[1].value.interpretedValue},
        {"attr": Object.keys(event.interpretations[0].intent.slots)[2],
            "value": Object.values(event.interpretations[0].intent.slots)[2].value.interpretedValue}
    ]});*/
    //numberofslots = Object.keys(event.interpretations[0].intent.slots).length;
    result = '';
    for (const [key, value] of Object.entries(event.interpretations[0].intent.slots)) {
        result += `${key}: ${value.value.interpretedValue}`;
    }
    return ServerReply (200, event, {"slots": result});
}

exports.handler = async (event) => {
	
	if (!event)
		return ServerReply (204);

	if (event.invocationSource !== 'FulfillmentCodeHook')
        return ServerReply (204, event);

    if (event.interpretations[0].intent.state !== 'ReadyForFulfillment')
        return ServerReply (204, event);

    if (event.interpretations[0].intent.name !== 'SearchDoctors')
        return ServerReply (204, event);

	return SearchDoctors (event);
}; 