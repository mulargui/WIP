const constants = require("./constants.js");
const mysql = require('mysql2/promise');
const axios = require('axios');

function ServerReply (code, event){
	
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
            //content: 'original event: ' + JSON.stringify(event) + '#end'
            content: 'intent: ' +  event.interpretations[0].intent.name
                + ' slot: ' +  Object.keys(event.interpretations[0].intent.slots)[0]
                + ' value: ' +  JSON.stringify(Object.values(event.interpretations[0].intent.slots)[0].value.interpretedValue) + '#end'
        }],
        sessionId: event.sessionId,
        requestAttributes: event.requestAttributes
    };
}

exports.handler = async (event) => {
	
	if (!event)
		return ServerReply (204, event);

	if (event.invocationSource !== 'FulfillmentCodeHook')
		return ServerReply (204, event);

	return ServerReply (200, event);
}; 