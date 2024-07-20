import config
import vision
import printer_manager
import phone_manager
import word_gen
from gcode import Gcode


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
    phone_manager.connect()

    print(printer_manager.start_position)

    # Start the printer
    while True:
        solve_wordle()


def solve_wordle():
    response = ""
    while response != "y" and response != "Y":
        response = input("Start a wordle game. Ready to start? [Ny] ")

    print("\n----- Taking Screenshot -----")
    phone_manager.screenshot()

    print("Screenshot aquired")

    print("Analyzing...")

    letter_data = vision.get_wheel()

    for letter in letter_data:
        print(f"Found letter '{letter}' at "
              + f"position(s): {letter_data[letter]}")

    print("Generating words...")

    letters = [letter[0] for letter in letter_data]
    words = word_gen.get_possibilities(letters)

    print("Found the words...")
    for word in words:
        print(word)

    print("Generating gcode...")
    gcode = Gcode()
    for word in words:
        gcode.hop_up()
        for letter in word:
            gcode.hop_down()
            letter_data[letter].append(position := letter_data[letter].pop(0))
            gcode.goto(position)

    print("Sending to printer...")
    print(gcode.get_code())

    input("Send to printer")
    printer_manager.send_script(gcode.get_code())


def main():
    setup()


if __name__ == "__main__":
    main()
