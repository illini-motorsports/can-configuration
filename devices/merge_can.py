"""
This is a utility script for merging .dbc files.
We often need to do this since software such as Racecon lets us export
a DBC file containing the messages the ECU (or any other device) intend to send.
We would like to make sure our master config file contains all these messages,
and as Vector's CANdb++ doesn't allow merging files in the free version
we can use this script to do so. 

Make sure you have the cantools Python library installed.
You can install this by running:

pip install cantools

in your shell.
"""

import cantools, glob

# Modify these variables to contain the input files you want to merge,
# and the final output file.
INPUT_FILES = glob.glob("*.dbc")
OUTPUT_FILE = "..\config.dbc"


# Sanity checks
if len(INPUT_FILES) <= 1 or len(OUTPUT_FILE) < 4:
    print("Invalid input/output file(s)!")
    exit()

# Load the first file as our base file
dbc = cantools.database.load_file(INPUT_FILES[0])

# Add each of the remaining files to our dbc
for i in range(1, len(INPUT_FILES)):
    dbc.add_dbc_file(INPUT_FILES[i])

# Write the output
cantools.database.dump_file(dbc, OUTPUT_FILE)