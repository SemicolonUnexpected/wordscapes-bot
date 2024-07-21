import subprocess


def connect():
    print("Starting adb...")

    subprocess.run(["adb", "start-server"], capture_output=True)
    subprocess.run(["adb", "detach"], capture_output=True)

    result = subprocess.run(["adb", "attach"], capture_output=True)

    print("Connecting...")

    if result.returncode == 1:
        print("Failed to connect to phone. Ensure it is connected via usb")
        exit(1)

    print("Connected\n")


def screenshot():
    result = subprocess.run(["adb", "exec-out", "screencap", "-p"],
                            capture_output=True)
    with open("screen.png", "wb") as fp:
        fp.write(result.stdout)
