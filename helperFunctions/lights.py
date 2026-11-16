import os
import uuid
import requests
from helperFunctions import getlightinfo

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
