import requests
import config
import json


def get_url():
    return f"http://{config.printer_ip}:{config.printer_port}"


def check_status():
    response = requests.get(get_url() + "/server/info")

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


def calibrate():
    readyness = check_status()
    print(readyness[1])

    if not readyness[0]:
        exit(1)

    # Home the printer to get accurate position information
    print("Homing...")
    home()

    # Configure the Z offset for the screen
    print("Ensure the stylus is just touching the top left corner of the screen")
    while True:
        value = input("Type in a height value for the printhead, or finish by typing 'Y' ")
        global screen_z_value

        try:
            screen_z_value = float(value)
            requests.post(get_url()
                          + f"/printer/gcode/script?script=G1 Z{
                          screen_z_value if screen_z_value > config.printer_min_z else config.printer_min_z}")
            print("Position: " + str(get_position()))
        except ValueError:
            if value == "y" or value == "Y":
                break

    print("Screen height calibrated Z:" + str(screen_z_value))


def get_position():
    response = requests.get(get_url()
                            + "/printer/objects/query?gcode_move=position")
    response = json.loads(response.text)
    return response["result"]["status"]["gcode_move"]["position"]


