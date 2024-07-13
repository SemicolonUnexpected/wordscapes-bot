import cv2 as cv
import numpy as np
import config
import printer_manager

def setup():
    # The title
    print("##### Wordscapes Bot ######\n");

    # Some setup data
    print("Before preceeding ensure the following configuration data is correct")
    
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

    print("\n----- Calibrating Printer ------")
    printer_manager.calibrate()

    



def main():
    setup()


if __name__ == "__main__":
    main()    
