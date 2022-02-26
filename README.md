# README

This folder contains the CAN configuration (DBC) files for the race vehicle. These files define the CAN messages across our bus, including IDs, signals, etc. 

The repo contains a single root file, `config.dbc`, which contains the "master" calibration. *This file should never be  modified directly!* It is primarily meant for tools like Vector CANalyzer to show you all the messages on the bus while plugged into the car. Generally, it is a better practice edit .DBC files for individual devices (see the `devices` folder). This allows us to more easily organize our bus as a combination of multiple components. It makes it easier to mass-rename signals, change all IDs for a device, etc. Use the script "merge_can.py" to merge all the DBC files for the individual devices into `config.dbc`. From the `devices` folder, you can just run `python merge_can.py`.

Original author: Aditya Mansharamani (aditya.mansha at gmail)