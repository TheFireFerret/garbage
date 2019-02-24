import json
from botocore.vendored import requests

URL = 'http://IP/'
def lambda_handler(event, context):
    request_type = event['request']['type']
    
    if request_type == "LaunchRequest":
        intent = "StartIntent"
    elif request_type == "IntentRequest":
        intent_type = event['request']['intent']['name']
        if intent_type == "StartIntent":
            intent = "StartIntent"
        else:
            intent = "StopIntent"



    try:
        req = requests.get(URL, timeout=2)
        state = req.text
        
        if intent == "StopIntent" or state == "stopping":
            answer = "Stopping sync!"
        else:
            answer = "Starting sync!"
        
        if req.status_code != 200:
            answer = "Sorry, Jasper broke something"
    except Exception as e:
        print("EXCEPTION")
        print(e)
        answer = "Sorry, Jasper broke something"
    
    return {
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': answer,
            }
        }
    }
