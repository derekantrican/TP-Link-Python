# TP-Link-Python

Examples of how to use the TP Link (Kasa) cloud API via Python. All examples are built on the great investigation & documentation by [itnerd.space](https://itnerd.space/)

## Getting started

1. Clone the repo
2. Open `settings.json` and fill in `email` and `password` with the credentials you use to log into https://tplinkcloud.com
3. Run `python getToken.py`. This will populate the `token` property in `settings.json`.
4. Run `python getDeviceList.py` to list your Kasa devices. Choose a device id from the output and populate the `deviceId` property in `settings.json`.

Now you're ready to use `getDeviceState.py` and `toggleSwitch.py`!
