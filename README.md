# MODBUS-ATTACK-SIMULATOR

Small modbus power plant simulation and modbus attack tool with output in German language.

Feel free to modify it.

The behavior of the power plant simulator is somewhat unrealistic, but the main point is to show how easy it is to attack Modbus systems. I recommend using ModbusPal as a modbus slave.
The attacker script modbuskiller changes all defined holding registers every 0.1 seconds.

Usage for both tools:

python3 modbus_kraftwerk.py

python3 modbus_killer_manual_ip.py

Start the tools, define ip address of the modbus slave and set the lower and upper register address of the address range (0 and 9 recommended).

Tested successfuly in Windows and Linux.

Dependencies: Python 3 Install pymodbusTCP library via pip install pymodbusTCP command.
