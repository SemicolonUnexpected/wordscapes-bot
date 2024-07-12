import requests
import config
import json


def get_url():
    return f"http://{config.printer_ip}:{config.printer_port}"


def check_response(response): # Ensure the response was good
    if response.status_code != requests.codes.ok:
        return False, f"Request failed - {response.status_code}"


def check_status():
    response = requests.get(get_url() + "/server/info")

    check_response(response)

    # Parse the json of the staus report from the server
    response = json.loads(response.text)

    # Check klipper is connected and ready
    if not response["result"]["klippy_connected"]:
        return False, "Klippy is not connected"

    if response["result"]["klippy_state"] != "ready":
        return False, "Klippy is not ready"

    return True, "Printer ready"

def home():
    response = requests.post(get_url()
        + "/printer/gcode/script?script=G28")

    check_response(response)

def get_position():
    response = requests.get(get_url()
        + "/printer/objects/query?gcode_move")

    check_response(response)

    print(response.text)

