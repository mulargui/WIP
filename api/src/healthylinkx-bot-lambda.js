const constants = require("./providers.js");

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
            //content: 'original event: ' + JSON.stringify(event) + ' #end' +
            content:    'results: ' + JSON.stringify(result) + ' #end'
        }],
        sessionId: event.sessionId,
        requestAttributes: event.requestAttributes
    };
}

function SearchDoctorsIntent (event){
    for (const [key, value] of Object.entries(event.interpretations[0].intent.slots)) {
        switch(key){
            case 'DoctorName':
                DoctorName = value.value.interpretedValue;
                break;
            case 'ZipCode':
                ZipCode = value.value.interpretedValue;
                break;
            case 'Gender':
                Gender = value.value.interpretedValue;
                break;
            default:
                return ServerReply(204, event);
        }
    }
    ret = SearchDoctors(DoctorName, ZipCode, Gender);
    return ServerReply(200, event, ret);
}

exports.handler = async (event) => {
	
	if (!event)
		return ServerReply(204);

	if (event.invocationSource !== 'FulfillmentCodeHook')
        return ServerReply(204, event);

    if (event.interpretations[0].intent.state !== 'ReadyForFulfillment')
        return ServerReply(204, event);

    if (event.interpretations[0].intent.name !== 'SearchDoctors')
        return ServerReply(204, event);

	return SearchDoctorsIntent(event);
}; 