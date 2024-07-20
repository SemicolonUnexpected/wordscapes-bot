import subprocess


def connect():
    subprocess.run(["adb", "start-server"])
    subprocess.run(["adb", "detach"])

    result = subprocess.run(["adb", "attach"], capture_output=True)

    if result.returncode == 1:
        print("Failed to connect to phone. Ensure it is connected via usb")
        exit(1)

    print("Connected")


def screenshot():
    result = subprocess.run(["adb", "exec-out", "screencap", "-p"],
                            capture_output=True)
    with open("screen.png", "wb") as fp:
        fp.write(result.stdout)
