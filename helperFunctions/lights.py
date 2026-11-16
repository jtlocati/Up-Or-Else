import os
import uuid
import requests
from helperFunctions import getlightinfo
import time

LIGHTINFO = [{"sku": f"{getlightinfo.SKU}", "device": f"{getlightinfo.DEVICE}"}]

def lightpower(unit, device_id, powerValue):
    FUNCTIONS = {
        "type": "devices.capabilities.on_off",
        "instance": "powerSwitch",
        "value": powerValue
    }

    payload = {
        "sku": unit,
        "device": device_id,
        "capability": FUNCTIONS
    }

    full_request = {
        "requestId": str(uuid.uuid4()),
        "payload": payload
    }

    try:
        responce = requests.post(getlightinfo.CONTROL_URL, headers=getlightinfo.header, json=full_request, timeout=50)
    except requests.RequestException:
        print("somthings arraie ;(")
        return False
    if responce.status_code != 200:
        print("nasty ahh responce:", responce.status_code)
        return False
    return True

def TurnOnLights(Value):
    device_list = getlightinfo.getLightInfo()
    lights_sucess = 0
    for light in device_list:
        sku = light["sku"]
        dev = light["device"]
        action = lightpower(sku, dev, Value)
        time.sleep(0.1)
        if action:
            lights_sucess+=1

    return lights_sucess


TurnOnLights(0)
