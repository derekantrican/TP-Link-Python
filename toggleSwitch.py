import sys
import json
import requests

with open('settings.json', 'r') as file:
    settings = json.load(file)

if not settings['token']:
    print('No token is set in settings.json. Please run `python getToken.py` first', file = sys.stderr)
    exit()

if not settings['deviceId']:
    print('No deviceId is set in settings.json. Please run `python getDeviceList.py` and choose a device id from that list', file = sys.stderr)
    exit()



url = f"https://wap.tplinkcloud.com?token={settings['token']}"

# First, get the device's current state
data = { 
    'method' : 'passthrough',
    'params' : {
        'deviceId' : settings['deviceId'],
        'requestData' : json.dumps({
            'system' : {
                'get_sysinfo' : None
            },
            'emeter' : {
                'get_realtime' : None
            }
        })
    }
}

response = requests.post(url, data = json.dumps(data))
responseJson = json.loads(response.text)
responseDataJson = json.loads(responseJson['result']['responseData'])
currentDeviceState = responseDataJson['system']['get_sysinfo']['relay_state']

# Next, send a request to set the state to the opposite of what it currently is (toggle)
# Reference: https://itnerd.space/2017/01/22/how-to-control-your-tp-link-hs100-smartplug-from-internet/

data = { 
    'method' : 'passthrough',
    'params' : {
        'deviceId' : settings['deviceId'],
        'requestData' : json.dumps({
            'system' : {
                'set_relay_state' : {
                    'state' : 0 if currentDeviceState == 1 else 1
                }
            }
        })
    }
 }

response = requests.post(url, data = json.dumps(data))
responseJson = json.loads(response.text)
responseDataJson = json.loads(responseJson['result']['responseData'])

print(json.dumps(responseJson, indent = 4))
print(json.dumps(responseDataJson, indent = 4))