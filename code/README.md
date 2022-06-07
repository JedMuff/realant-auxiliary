## Code Notes
The following scripts are used to test and control the robot:
-	antproxy.py
-	ant_server.py
-	tester.py
-	commander.py
-	move_set.py

The **antproxy.py** and **ant_sever.py** scripts are used to set up communication with the robot using ZeroMQ. 
These scripts are unchanged from the versions used in the original RealAnt, except for row 20 in **ant_server.py**.
which should be modified to reflect the port used for the USB connection to the robot.

The **tester.py** script is used to test individual servos, selected by their Dynamixel ID. 
The code contains functions for writing a position to a servo, testing the full motion range of a servo, and resetting 
the servos to their default positions. The script prints messages to the terminal to guide the user.

The **commander.py** requires the “keyboard” Python library. It contains functions for pre-programmed linear and rotational motion. 
The script also calls other pre-programmed actions stored in the **move_set.py** file. The W, A, S and D keys are used for linear motion,  
Q is used for counter-clockwise rotation and E for clockwise rotation, and keys 1-9 are used to run pre-programmed actions 
stored in the **move_set.py** file.

How to use:
1)	Connect power supply and USB to the robot
2)	Change line 20 in **ant_server.py** to reflect the USB port used. Default is /dev/ttyACM0.
3)	Run from the command line the following scripts: **antproxy.py**, **ant_server.py**, and **tester.py** or **commander.py**

The **ant11_cmd_dxl.ino** is the Arduino code for the OpenCM9.04 control board, and it is unchanged from the version found in the original RealAnt.

The .ino files in the folders "general_test_codes" and "servo_config_code" are not needed to run the robot, but they can be used to configure and test Dynamixel AX-12A servos via the OpenCM9.04 control board. More details are found under **/docs/dynamixel_A12A_guide.md** heading **'Accessing the Control Table via the OpenCM9.04 controller'**.
