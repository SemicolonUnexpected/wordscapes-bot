from ppadb.client import Client as AdbClient

ip = "192.168.1.105"
port = 34151

client = AdbClient(host="127.0.0.1", port=5037)
client.remote_connect(ip, port)
device = client.device(ip + ":" + str(port))

result = device.screencap()
with open("screen.png", "wb") as fp:
    fp.write(result)

# Disconnect all devices
client.remote_disconnect()

##Disconnect 172.20.0.1
# client.remote_disconnect("172.20.0.1")
##Or
# client.remote_disconnect("172.20.0.1", 5555)
