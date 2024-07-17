import config
import vision
import printer_manager
import phone_manager


def setup():
    # The title
    print("##### Wordscapes Bot ######\n")

    # Some setup data
    print("Before preceeding ensure the following"
          + "configuration data is correct")

    # Print out some of the configuration info
    print("----- Phone -----\n"
          + f"Size: {config.phone_width}mm x {config.phone_height}mm\n"
          + f"IP: {config.phone_ip}\n"
          + f"Port: {config.phone_port}\n")

    print("----- Printer -----\n"
          + f"IP: {config.printer_ip}\n"
          + f"Port: {config.printer_port}\n")

    # Await a start command
    response = ""
    while response != "y" and response != "Y":
        response = input("Ready to setup? [Ny] ")

    # Connect the hardware
    print("\n----- Calibrating Printer ------")
    printer_manager.calibrate()

    print("\n----- Connecting to phone -----")
    printer_manager.connect()

    # Start the printer
    while True:
        solve_wordle()


def solve_wordle():
    response = ""
    while response != "y" and response != "Y":
        response = input("Start a wordle game. Ready to start? [Ny] ")

    print("\n ##### Starting #####")

    print("\n----- Taking Screenshot -----")
    phone_manager.screenshot()
    print("Screenshot aquired")

    print("Analyzing...")

    letters = vision.get_wheel()

    for letter in letters:
        print(f"Found letter '{letters[0]}' at "
              + f"position: {round(letter[1], 2)}mm from the top left")


def main():
    setup()


if __name__ == "__main__":
    main()
