import cantools


CONFIG_FILE = "config.dbc"
MKDWN_FILE = "README.md"

HEADER_MSG = """\
This folder contains the CAN configuration (DBC) files for the race vehicle. These files define the CAN messages across our bus, including IDs, signals, etc.

The repo contains a single root file, `config.dbc`, which contains the "master" calibration. *This file should never be  modified directly!* It is primarily meant for tools like Vector CANalyzer to show you all the messages on the bus while plugged into the car. Generally, it is a better practice edit .DBC files for individual devices (see the `devices` folder). This allows us to more easily organize our bus as a combination of multiple components. It makes it easier to mass-rename signals, change all IDs for a device, etc. Use the script "merge_can.py" to merge all the DBC files for the individual devices into `config.dbc`. From the `devices` folder, you can just run `python merge_can.py`.

Original author: Aditya Mansharamani (aditya.mansha at gmail)

---
"""


# Open overall config database
dbc = cantools.database.load_file(CONFIG_FILE)

out_file = open(MKDWN_FILE, "w")
out_file.write(HEADER_MSG)

for message in dbc.messages:
    out_file.write(f"## {message._name}\n\n")
    out_file.write(f"### ID: 0x{message._frame_id:x} -- Length: {message._length} Bytes -- Extended: {'Yes' if message._is_extended_frame else 'No'}\n\n")
    out_file.write(f"| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |\n")
    out_file.write(f"| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |\n")
    for s in message.signals:
        out_file.write(f"| {s.name} | {s.start} | {s.length} | {s.byte_order} | {'Yes' if s.is_signed else 'No'} | {s.initial} |"\
                       f"{s.scale} | {s.minimum} | {s.maximum} | {s.unit} |\n")


out_file.close()