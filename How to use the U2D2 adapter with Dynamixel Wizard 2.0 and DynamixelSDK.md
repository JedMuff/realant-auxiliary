# How to use the U2D2 adapter with Dynamixel Wizard 2.0 and DynamixelSDK

## Connections:
1)	Connect the U2D2 to the computer via the provided USB-MicroUSB cable.
2)	Connect the U2D2 to the Dynaxmixel AX-12A servo using the 3-pin TTL cable.
3)	Power the servo(s) with a switched-mode power supply (SMPS), via the SMPS2Dynamixel board, using another 3-pin cable.
         
## Configuring the servo in Dynamixel Wizard 2.0
Install the DynamixelWizard 2.0 program following the instructions for your operating system in https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/.  
In the wizard click options and select for which settings you want to scan for servos:
 
For example, the range of baud rates or IDs can be reduced for faster if you know what you are looking for. Scan for Dynamixels. When the servo(s) you have connected are found you will see a list of Dynamixels to the left and the settings of the chosen servo in the middle of the screen:

To change a parameter, select the parameter from the list, select a value from the list opening in the bottom right corner, and press “Save”. The following picture shows changing the ID to 2. Other parameter settings can be changed in a similar way.
 
In the **top right corner**, you can turn the indicator led on the servo on and off, and you can **rotate the servo to a chosen position by clicking on the black/grey/red dial.**

## Using the DynamixelSDK library 
Using the U2D2 you can directly run Python code for the Dynamixel servos. Example code can be found in the DynamixelSDK GitHub https://github.com/ROBOTIS-GIT/DynamixelSDK. For example, the **DynamixelSDK > python > tests > protocol1_0 > read_write.py** example can be used to get the servo rotating between the minimum and maximum position set in the code. However, first the correct parameters for the AX-12A model servo must be set by modifying the code:
ADDR_MX_TORQUE_ENABLE = 24
ADDR_MX_GOAL_POSITION = 30
ADDR_MX_PRESENT_POSITION   = 36
DXL_ID	= 1 #or something else if it has been changed
BAUDRATE = 1000000 #or e.g. 57600 if it has been changed
DXL_MAXIMUM_POSITION_VALUE  = 1023 #changed from 4000, as 1023 is the maximum for AX-12A
DEVICENAME = 'COM10' #or something else depending on the port and OS used in the computer

To use the DynamixelSDK examples you must install the library, for example by running **“pip install dynamixel_sdk” on Windows.** 

## For more information see:
U2D2 e-Manual: https://emanual.robotis.com/docs/en/parts/interface/u2d2/  
SMPS2Dynamixel: https://www.robotis.us/smps2dynamixel/  
Dynamixel Wizard 2.0 e-Manual: https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/  
DynamixelSDK: https://github.com/ROBOTIS-GIT/DynamixelSDK  

