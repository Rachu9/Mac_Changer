MAC Address Changer Script
This Python script allows you to change the MAC address of a network interface on a Unix-like operating system. It utilizes system commands to configure the network interface.

Prerequisites
Python 3: Ensure Python 3 is installed on your system.
Root Privileges: Changing the MAC address requires root or administrator access.
Usage Instructions
Download the Script:

Obtain the script file from the repository or source.
Run the Script:

Open a terminal on your system.
Navigate to the directory containing the script.
Execute the script with root privileges using the command:
bash
Copy code
sudo python3 mac_changer.py
Provide Required Inputs:

When prompted, enter:
Interface: The name of the network interface you wish to modify (e.g., eth0, wlan0).
New MAC: The new MAC address you want to set (e.g., 00:11:22:33:44:55).
Example Usage
After running the script and providing the required inputs, the MAC address of the specified interface will be changed to the new address you provided.
