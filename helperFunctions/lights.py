import os
import uuid
import requests
from helperFunctions import getlightinfo

LIGHTINFO = [{"sku": f"{getlightinfo.SKU}", "device": f"{getlightinfo.DEVICE}"}]

def lightpower(powerValue):
    FUNCTIONS = {
        "type": "devices.capabilities.on_off",
        "instance": "powerSwitch",
        "value": powerValue
    }

    payload = {
        "sku": getlightinfo.SKU,
        "device": getlightinfo.DEVICE,
        "capability": FUNCTIONS
    }

    full_request = {
        "requestID": str(uuid.uuid4()),
        "payload": payload
    }

    try:
        responce = requests.post(getlightinfo.CONTROL_URL, headers=getlightinfo.header, json=full_request, timeout=50)
    except requests.RequestException:
        print("somthings arraie ;(")
        return False
    if responce.status_code != 200:
        print("nasty ahh responce")
        return False
    return True

def TurnOnLights():
    for light in LIGHTINFO:
        lightpower(1)


TurnOnLights()
