from ppadb.client import Client as AdbClient
import config


# The adb client
client = None
# The connected device
device = None


def connect():
    global device
    global client

    print("Connecting...")
    client = AdbClient("127.0.0.1", port=config.client_port)
    client.remote_connect(config.phone_ip, config.phone_port)

    device = client.device(config.phone_ip + ":"
                           + str(config.phone_port))

    print("Connected.")


def disconnect():
    global client
    client.remote_disconnect()  # Disconnect from all devices


def screenshot():
    global device
    result = device.screencap()
    with open("screen/screen.png", "wb") as fp:
        fp.write(result)
