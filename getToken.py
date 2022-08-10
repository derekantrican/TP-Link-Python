import sys
import requests
import json

with open('settings.json', 'r') as file:
    settings = json.load(file)

if not settings['email'] or not settings['password']:
    print('Please set the email & password variables in settings.json using your https://tplinkcloud.com/ credentials', file = sys.stderr)
    exit()

# Reference: https://itnerd.space/2017/06/19/how-to-authenticate-to-tp-link-cloud-api/

url = 'https://wap.tplinkcloud.com'
data = { 
    'method' : 'login',
    'params' : {
        'appType' : 'Kasa_Android',
        'cloudUserName' : settings['email'],
        'cloudPassword' : settings['password'],
        'terminalUUID' : '7218c95b-aa76-4654-8c9c-545466672961' # This can be any UUIDv4 (you can generate one from https://www.uuidgenerator.net/version4)
    }
}

response = requests.post(url, data = json.dumps(data))
responseJson = json.loads(response.text)

print(json.dumps(responseJson, indent = 4))

settings['token'] = responseJson['result']['token']
with open('settings.json', 'w') as file:
    file.write(json.dumps(settings, indent = 4))