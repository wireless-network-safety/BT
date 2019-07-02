# Commands:
# $ hciconfig
# $ hciconfig NAME up
# $ hciconfig

# pip install PrettyTable
from prettytable import PrettyTable
from bluetooth import *
import argparse

# function that scans bluetooth devices
def FindDevices(_duration):
    # use table to display devices
    BTable = PrettyTable(['Index', 'Bluetooth Address', 'Bluetooth Name'])
    nearby_devices = discover_devices(duration = _duration)
    for (i, address) in enumerate(nearby_devices):
        BTable.add_row([str(i+1), address, lookup_name(address)])
    print BTable


if __name__ == "__main__":
    # construct the argument and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--duration", type = int, default = 3,
                    help="duration for finding bluetooth devices command")
    args = vars(ap.parse_args())

    # scan devices
    FindDevices(args["duration"])

