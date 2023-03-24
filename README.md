This folder contains the CAN configuration (DBC) files for the race vehicle. These files define the CAN messages across our bus, including IDs, signals, etc.

The repo contains a single root file, `config.dbc`, which contains the "master" calibration. *This file should never be  modified directly!* It is primarily meant for tools like Vector CANalyzer to show you all the messages on the bus while plugged into the car. Generally, it is a better practice edit .DBC files for individual devices (see the `devices` folder). This allows us to more easily organize our bus as a combination of multiple components. It makes it easier to mass-rename signals, change all IDs for a device, etc. Use the script "merge_can.py" to merge all the DBC files for the individual devices into `config.dbc`. From the `devices` folder, you can just run `python merge_can.py`.

Original author: Aditya Mansharamani (aditya.mansha at gmail)

---
## ECU_General

### ID: 0x300 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| nmot | 7 | 16 | big_endian | Yes | None |1 | 0 | 20000 | rpm |
| ath | 23 | 16 | big_endian | Yes | None |0.1 | 0 | 110 | % |
| lambda | 39 | 16 | big_endian | Yes | None |0.001 | 0 | 5 | None |
| ub | 55 | 16 | big_endian | Yes | None |0.01 | 0 | 25.5 | V |
## ECU_Pressures

### ID: 0x302 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| pamb | 0 | 16 | little_endian | No | None |0.1 | 0 | 2000 | mbar |
| poil | 23 | 16 | big_endian | Yes | None |0.001 | 0 | 10 | bar |
| p22 | 39 | 16 | big_endian | Yes | None |1 | 0 | 5000 | mbar |
| pfuel | 55 | 16 | big_endian | Yes | None |0.001 | 0 | 10 | bar |
## ECU_Temps

### ID: 0x301 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| tmot | 0 | 8 | little_endian | No | None |1 | 40 | 120 | °C |
| toil | 15 | 8 | big_endian | No | None |1 | 60 | 150 | °C |
| tint | 23 | 8 | big_endian | No | None |1 | 10 | 60 | °C |
| tfuel | 31 | 8 | big_endian | No | None |1 | 10 | 80 | °C |
| texh | 32 | 16 | little_endian | No | None |1 | 0 | 1250 | °C |
## ECU_Power_Control

### ID: 0x20 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| Engine_Cranking | 0 | 8 | little_endian | No | None |1 | 0 | 1 | None |
| Engine_Running | 8 | 8 | little_endian | No | None |1 | 0 | 1 | None |
| tmot | 16 | 8 | little_endian | No | None |1 | 40 | 120 | °C |
| nmot | 24 | 16 | little_endian | No | None |1 | 0 | 20000 | rpm |
| gear | 40 | 8 | little_endian | Yes | None |1 | -1 | 12 | None |
| pbrake_f | 48 | 8 | little_endian | No | None |1 | 0 | 150 | bar |
| pbrake_r | 56 | 8 | little_endian | No | None |1 | 0 | 150 | bar |
## ECU_Gear_Control

### ID: 0x3fb -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| speed | 0 | 16 | little_endian | No | None |0.01 | 0 | 400 | km/h |
| nmot | 16 | 16 | little_endian | Yes | None |1 | 0 | 20000 | rpm |
## ECU_INT_Sw_Rot_01_SDM102

### ID: 0x620 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| SDM102_ECU_Map | 8 | 8 | little_endian | No | None |1 | None | None | None |
| SDM102_Tract_Ctrl | 40 | 8 | little_endian | No | None |1 | None | None | None |
## ECU_INT_Sw_Bin_01_SDM102

### ID: 0x628 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| SDM102_Launch_Ctrl_On | 3 | 1 | little_endian | No | None |1 | 0 | 1 | None |
## ECU_Switches

### ID: 0x3fe -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| mappos | 0 | 8 | little_endian | No | None |1 | 0 | 15 | None |
| tcstage | 8 | 8 | little_endian | No | None |1 | 0 | 12 | None |
| B_launch | 16 | 8 | little_endian | No | None |1 | 0 | 1 | None |
| GCM_Autoupshifting_Enabled | 24 | 8 | little_endian | No | None |1 | 0 | 1 | None |
## ECU_Lap_Times

### ID: 0x69a -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| Laptrigger_laptimeold_dls | 0 | 32 | little_endian | No | None |0.01 | 0 | 500 | s |
| Laptrigger_laptime_dls | 32 | 32 | little_endian | No | None |0.01 | 0 | 500 | s |
## ECU_Lap_Times_2

### ID: 0x69b -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| Laptrigger_lapdiff_dls | 0 | 16 | little_endian | Yes | None |0.01 | -20 | 20 | s |
| Laptrigger_lapdiffb_dls | 16 | 16 | little_endian | Yes | None |0.01 | -20 | 20 | s |
| Laptrigger_laptimebest_dls | 32 | 32 | little_endian | No | None |0.01 | 0 | 500 | s |
## ECU_Lap_Times_3

### ID: 0x69c -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| lapctr | 0 | 8 | little_endian | No | None |1 | 0 | 255 | None |
| outctr | 8 | 8 | little_endian | No | None |1 | 0 | 255 | None |
## ECU_Wheel_Speeds

### ID: 0x3aa -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| vwheel_fl | 0 | 8 | little_endian | No | None |1 | 0 | 400 | km/h |
| vwheel_fr | 8 | 8 | little_endian | No | None |1 | 0 | 400 | km/h |
| vwheel_rl | 16 | 8 | little_endian | No | None |1 | 0 | 400 | km/h |
| vwheel_rr | 24 | 8 | little_endian | No | None |1 | 0 | 400 | km/h |
| speed | 32 | 8 | little_endian | No | None |1 | 0 | 400 | km/h |
## ECU_Autoupshifting_Targets_1

### ID: 0x250 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
## ECU_Autoupshifting_Targets_3

### ID: 0x252 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
## ECU_Autoupshifting_Targets_2

### ID: 0x251 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
## ECU_Gear_Control_2

### ID: 0x3fc -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| SDM102_Autoupshifting_On | 0 | 8 | little_endian | No | None |1 | 0 | 1 | None |
## IZZE_Brake_IR_Programming

### ID: 0x7af -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
## GCM_Autoupshifting

### ID: 0x203 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| GCM_RPM | 0 | 16 | little_endian | No | None |1 | None | None | None |
| GCM_AU_Target_RPM | 16 | 16 | little_endian | No | None |1 | None | None | None |
| GCM_Speed | 32 | 8 | little_endian | No | None |1 | None | None | None |
| GCM_AU_Target_Speed | 40 | 8 | little_endian | No | None |1 | None | None | None |
| GCM_RPM_Delay_Adjustment | 48 | 8 | little_endian | No | None |1 | None | None | None |
| GCM_Wheel_Speed_Delay_Adjustment | 56 | 8 | little_endian | No | None |0.01 | None | None | None |
## GCM_MS6_Gearcut

### ID: 0x610 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| GCM_Downshift_MS6 | 0 | 1 | little_endian | No | None |1 | None | None | None |
| GCM_Upshift_MS6 | 1 | 1 | little_endian | No | None |1 | None | None | None |
## GCM_Queue

### ID: 0x202 -- Length: 4 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| GCM_Switch_Up | 0 | 1 | little_endian | No | None |1 | None | None | None |
| GCM_Switch_Down | 1 | 1 | little_endian | No | None |1 | None | None | None |
| GCM_Switch_Neutral | 2 | 1 | little_endian | No | None |1 | None | None | None |
| GCM_UpshiftQueue | 8 | 8 | little_endian | No | None |1 | None | None | None |
| GCM_DownshiftQueue | 16 | 8 | little_endian | No | None |1 | None | None | None |
| GCM_NeutralQueue | 24 | 8 | little_endian | No | None |1 | None | None | None |
## GCM_Gear

### ID: 0x201 -- Length: 6 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| GCM_Gear | 0 | 8 | little_endian | No | None |1 | None | None | None |
| GCM_Mode | 8 | 8 | little_endian | No | None |1 | None | None | None |
| GCM_Gear_Sensor_Voltage | 16 | 16 | little_endian | No | None |0.0001 | None | None | V |
| GCM_Shift_Force | 32 | 16 | little_endian | Yes | None |0.01 | None | None | N |
## GCM_Error

### ID: 0xf -- Length: 4 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| GCM_ERR_Origin_Node | 0 | 16 | little_endian | No | None |1 | None | None | None |
| GCM_ERR_Code | 16 | 16 | little_endian | No | None |1 | None | None | None |
## GCM_Temps

### ID: 0x200 -- Length: 6 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| GCM_Uptime | 0 | 16 | little_endian | No | None |1 | None | None | s |
| GCM_PCB_Temp | 16 | 16 | little_endian | Yes | None |0.005 | None | None | C |
| GCM_IC_Temp | 32 | 16 | little_endian | Yes | None |0.005 | None | None | C |
## IMU_Z

### ID: 0x17c -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IMU_Z_Accel | 32 | 16 | little_endian | No | None |0.0001274 | None | None | g |
## IMU_X_Roll

### ID: 0x178 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IMU_Roll_Rate | 0 | 16 | little_endian | No | None |0.005 | None | None | deg/s/s |
| IMU_X_Accel | 32 | 16 | little_endian | No | None |0.0001274 | None | None | g |
## IMU_Y_Yaw

### ID: 0x174 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IMU_Yaw_Rate | 0 | 16 | little_endian | No | None |0.005 | None | None | deg/s |
| IMU_Y_Accel | 32 | 16 | little_endian | No | None |0.0001274 | None | None | g |
## PDM_Status_3

### ID: 0x402 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| PDM_Ignition_Current | 0 | 8 | little_endian | No | None |1 | 0 | 255 | None |
| PDM_CAN_Current | 8 | 8 | little_endian | No | None |1 | 0 | 255 | None |
| PDM_Water_Pump_Current | 16 | 8 | little_endian | No | None |1 | 0 | 255 | None |
| PDM_Extra_Current | 24 | 8 | little_endian | No | None |1 | 0 | 255 | None |
## PDM_Status_2

### ID: 0x401 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| PDM_F_BSPD_Error | 0 | 8 | little_endian | No | None |1 | None | None | None |
| PDM_F_BSPD_Enable | 8 | 8 | little_endian | No | None |1 | None | None | None |
| PDM_Actuator_Down_Current | 16 | 8 | little_endian | No | None |1 | 0 | 255 | None |
| PDM_Actuator_Up_Current | 24 | 8 | little_endian | No | None |1 | 0 | 255 | None |
| PDM_ECU_Current | 32 | 8 | little_endian | No | None |1 | 0 | 255 | None |
| PDM_Fan_Current | 40 | 8 | little_endian | No | None |1 | 0 | 255 | None |
| PDM_Fuel_Pump_Current | 48 | 8 | little_endian | No | None |1 | 0 | 255 | None |
| PDM_Ignition_Current | 56 | 8 | little_endian | No | None |1 | 0 | 255 | None |
## PDM_Status_1

### ID: 0x400 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| PDM_Total_Current | 0 | 8 | little_endian | No | None |1 | 0 | 255 | None |
| PDM_Fan_Active | 8 | 8 | little_endian | No | None |1 | None | None | None |
| PDM_Water_Pump_Active | 16 | 8 | little_endian | No | None |1 | None | None | None |
| PDM_SW_Shift_Down | 40 | 8 | little_endian | No | None |1 | 0 | 255 | None |
| PDM_SW_Shift_Up | 48 | 8 | little_endian | No | None |1 | 0 | 255 | None |
## SDM550_GPS_Heading

### ID: 0x691 -- Length: 4 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| SDM550_GPS_Heading | 7 | 32 | big_endian | Yes | None |0.01 | None | None | deg |
## SDM550_GPS_LatLong

### ID: 0x690 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| SDM550_GPS_Lat | 7 | 32 | big_endian | Yes | None |1e-07 | None | None | deg |
| SDM550_GPS_Long | 39 | 32 | big_endian | Yes | None |1e-07 | None | None | deg |
## SDM550_LapTrigger

### ID: 0x5 -- Length: 2 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| SDM550_Lap_Trigger | 0 | 16 | little_endian | Yes | None |1 | None | None | None |
## SDM102_Knobs

### ID: 0x6ae -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| SDM102_ECU_Map | 0 | 16 | little_endian | Yes | None |1 | None | None | None |
| SDM102_Launch_Ctrl_AU | 16 | 16 | little_endian | Yes | None |1 | None | None | None |
| SDM102_Tract_Ctrl | 32 | 16 | little_endian | Yes | None |1 | None | None | None |
| SDM102_Page_Control | 48 | 16 | little_endian | Yes | None |1 | None | None | None |
## IZZE_Brake_IR_4C9_Status

### ID: 0x4cd -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_Brake_IR_4C9_Internal_Temp | 7 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
## IZZE_Brake_IR_4C9_Ch13to16

### ID: 0x4cc -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_Brake_IR_4C9_Channel_13 | 7 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_4C9_Channel_14 | 23 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_4C9_Channel_15 | 39 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_4C9_Channel_16 | 55 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
## IZZE_Brake_IR_4C9_Ch9to12

### ID: 0x4cb -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_Brake_IR_4C9_Channel_10 | 7 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_4C9_Channel_11 | 23 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_4C9_Channel_12 | 39 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_4C9_Channel_9 | 55 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
## IZZE_Brake_IR_4C9_Ch5to8

### ID: 0x4ca -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_Brake_IR_4C9_Channel_5 | 7 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_4C9_Channel_6 | 23 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_4C9_Channel_7 | 39 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_4C9_Channel_8 | 55 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
## IZZE_Brake_IR_4C9_Ch1to4

### ID: 0x4c9 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_Brake_IR_4C9_Channel_1 | 7 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_4C9_Channel_2 | 23 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_4C9_Channel_3 | 39 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_4C9_Channel_4 | 55 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
## IZZE_Brake_IR_7A0_Status

### ID: 0x7a4 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_Brake_IR_7A0_Internal_Temp | 7 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
## IZZE_Brake_IR_7A0_Ch13to16

### ID: 0x7a3 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_Brake_IR_7A0_Channel_13 | 7 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_7A0_Channel_14 | 23 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_7A0_Channel_15 | 39 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_7A0_Channel_16 | 55 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
## IZZE_Brake_IR_7A0_Ch9to12

### ID: 0x7a2 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_Brake_IR_7A0_Channel_10 | 7 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_7A0_Channel_11 | 23 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_7A0_Channel_12 | 39 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_7A0_Channel_9 | 55 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
## IZZE_Brake_IR_7A0_Ch5to8

### ID: 0x7a1 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_Brake_IR_7A0_Channel_5 | 7 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_7A0_Channel_6 | 23 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_7A0_Channel_7 | 39 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_7A0_Channel_8 | 55 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
## IZZE_Brake_IR_7A0_Ch1to4

### ID: 0x7a0 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_Brake_IR_7A0_Channel_1 | 7 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_7A0_Channel_2 | 23 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_7A0_Channel_3 | 39 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
| IZZE_Brake_IR_7A0_Channel_4 | 55 | 16 | big_endian | No | None |0.1 | 0 | 65535 | C |
## IZZE_SG_4E2

### ID: 0x4e2 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_SG_4E2_Differential_Voltage | 7 | 16 | big_endian | Yes | None |1 | None | None | µV |
| IZZE_SG_4E2_Calibrated_Output | 23 | 16 | big_endian | Yes | None |0.1 | None | None | F |
| IZZE_SG_4E2_Internal_Temperature | 39 | 16 | big_endian | Yes | None |0.1 | None | None | C |
| IZZE_SG_4E2_External_Temperature | 55 | 16 | big_endian | Yes | None |0.1 | None | None | C |
## IZZE_SG_4E4

### ID: 0x4e4 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_SG_4E4_Differential_Voltage | 7 | 16 | big_endian | Yes | None |1 | None | None | µV |
| IZZE_SG_4E4_Calibrated_Output | 23 | 16 | big_endian | Yes | None |0.1 | None | None | F |
| IZZE_SG_4E4_Internal_Temperature | 39 | 16 | big_endian | Yes | None |0.1 | None | None | C |
| IZZE_SG_4E4_External_Temperature | 55 | 16 | big_endian | Yes | None |0.1 | None | None | C |
## IZZE_SG_4E5

### ID: 0x4e5 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_SG_4E5_Differential_Voltage | 7 | 16 | big_endian | Yes | None |1 | None | None | µV |
| IZZE_SG_4E5_Calibrated_Output | 23 | 16 | big_endian | Yes | None |0.1 | None | None | F |
| IZZE_SG_4E5_Internal_Temperature | 39 | 16 | big_endian | Yes | None |0.1 | None | None | C |
| IZZE_SG_4E5_External_Temperature | 55 | 16 | big_endian | Yes | None |0.1 | None | None | C |
## IZZE_SG_4E6

### ID: 0x4e6 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_SG_4E6_Differential_Voltage | 7 | 16 | big_endian | Yes | None |1 | None | None | ï¿½V |
| IZZE_SG_4E6_Calibrated_Output | 23 | 16 | big_endian | Yes | None |0.1 | None | None | F |
| IZZE_SG_4E6_Internal_Temperature | 39 | 16 | big_endian | Yes | None |0.1 | None | None | C |
| IZZE_SG_4E6_External_Temperature | 55 | 16 | big_endian | Yes | None |0.1 | None | None | C |
## IZZE_SG_4E7

### ID: 0x4e7 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_SG_4E7_Differential_Voltage | 7 | 16 | big_endian | Yes | None |1 | None | None | µV |
| IZZE_SG_4E7_Calibrated_Output | 23 | 16 | big_endian | Yes | None |0.1 | None | None | F |
| IZZE_SG_4E7_Internal_Temperature | 39 | 16 | big_endian | Yes | None |0.1 | None | None | C |
| IZZE_SG_4E7_External_Temperature | 55 | 16 | big_endian | Yes | None |0.1 | None | None | C |
## IZZE_WLSG_429

### ID: 0x429 -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_WLSG_429_Out | 7 | 16 | big_endian | Yes | None |-1 | None | None | uV |
| IZZE_WLSG_429_VBAT | 23 | 16 | big_endian | Yes | None |0.001 | None | None | V |
| IZZE_WLSG_429_Temp | 39 | 16 | big_endian | Yes | None |0.1 | None | None | C |
| IZZE_WLSG_429_RSSI | 55 | 16 | big_endian | Yes | None |1 | None | None | dBm |
## IZZE_WLSG_42A

### ID: 0x42a -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| IZZE_WLSG_42A_Out | 7 | 16 | big_endian | Yes | None |1 | None | None | uV |
| IZZE_WLSG_42A_VBAT | 23 | 16 | big_endian | Yes | None |0.001 | None | None | V |
| IZZE_WLSG_42A_Temp | 39 | 16 | big_endian | Yes | None |0.1 | None | None | C |
| IZZE_WLSG_42A_RSSI | 55 | 16 | big_endian | Yes | None |1 | None | None | dBm |
## Kistler_S350_C

### ID: 0x7fc -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| Kistler_S350_SerialNo | 7 | 32 | big_endian | No | None |1 | 0 | 4294970000 | None |
| Kistler_S350_TempSens | 39 | 8 | big_endian | Yes | None |1 | -128 | 127 | °C |
| Kistler_S350_CurrLED | 47 | 8 | big_endian | No | None |0.01 | 0 | 2.55 | A |
| Kistler_S350_PowerOK | 55 | 1 | big_endian | No | None |1 | 0 | 1 | None |
| Kistler_S350_CurrOK | 54 | 1 | big_endian | No | None |1 | 0 | 1 | None |
| Kistler_S350_CurrHigh | 53 | 1 | big_endian | No | None |1 | 0 | 1 | None |
| Kistler_S350_OpticOK | 52 | 1 | big_endian | No | None |1 | 0 | 1 | None |
| Kistler_S350_TempOK | 51 | 1 | big_endian | No | None |1 | 0 | 1 | None |
| Kistler_S350_SensorOK | 50 | 1 | big_endian | No | None |1 | 0 | 1 | None |
| Kistler_S350_FilerON | 49 | 1 | big_endian | No | None |1 | 0 | 1 | None |
| Kistler_S350_StSt | 48 | 1 | big_endian | No | None |1 | 0 | 1 | None |
| Kistler_S350_FilterSetting | 63 | 7 | big_endian | No | None |1 | 0 | 127 | None |
| Kistler_S350_FilterType | 56 | 1 | big_endian | No | None |1 | 0 | 1 | None |
## Kistler_S350_B

### ID: 0x7fb -- Length: 6 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| Kistler_S350_VelX | 7 | 16 | big_endian | No | None |0.036 | 0 | 400 | km/h |
| Kistler_S350_VelY | 23 | 16 | big_endian | Yes | None |0.036 | -100 | 100 | km/h |
| Kistler_S350_Angle | 39 | 16 | big_endian | Yes | None |0.01 | -45 | 45 | ° |
## Kistler_S350_A

### ID: 0x7fa -- Length: 8 Bytes -- Extended: No

| Name | Start Bit | Length | Byte Order | Signed | Initial | Scale | Minimum | Maximum | Unit |
| ---- | ---------- | ------ | ---------- | ------ | ------- | ----- | ------- | ------- | ---- |
| Kistler_S350_Timestamp | 7 | 16 | big_endian | No | None |1 | 0 | 65535 | None |
| Kistler_S350_Vel | 23 | 16 | big_endian | No | None |0.036 | 0 | 400 | km/h |
| Kistler_S350_Dist | 39 | 32 | big_endian | No | None |0.001 | 0 | 4294970 | m |
