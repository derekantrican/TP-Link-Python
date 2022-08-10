import sys
import json
import requests

with open('settings.json', 'r') as file:
    settings = json.load(file)

if not settings['token']:
    print('No token is set in settings.json. Please run `python getToken.py` first', file = sys.stderr)
    exit()

# Reference: https://itnerd.space/2017/05/21/how-to-get-the-tp-link-hs100-cloud-end-point-url/

url = f"https://wap.tplinkcloud.com?token={settings['token']}"
data = { 
    'method' : 'getDeviceList',
}

response = requests.post(url, data = json.dumps(data))
responseJson = json.loads(response.text)

print(json.dumps(responseJson, indent = 4))