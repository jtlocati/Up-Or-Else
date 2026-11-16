import os
import uuid
import requests

GOVEE_KEEY = os.getenv("GOVEE_KEEY")

#define endopoints:
DEVICES_URL = "https://openapi.api.govee.com/router/api/v1/user/devices"
CONTROL_URL = "https://openapi.api.govee.com/router/api/v1/device/control"

LIGHTINFO = [{"sku": "", "device": ""}]
header = {
    "Govee-API-Key": GOVEE_KEEY,
    "Content-Type": "application/json"
}

def getLightInfo() -> dict:
    try:
        responce = requests.get(DEVICES_URL, headers=header, timeout=50)
    except requests.RequestException:
        print("somth is broken ong")
        return []

    #test 200 4 nowm docs do not confirm if this is actually the real good stat code, but i trust
    if responce.status_code != 200:
        print("error gained on responsce")
        return []

    device_ID = responce.json().get("data", [])
    return device_ID

devie_ID = getLightInfo()

print(devie_ID)