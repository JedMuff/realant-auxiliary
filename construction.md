# Preliminary Configuration of the Electronic Parts
## OpenCM9.04 Board

1.	U2D2 adapter or Arduino Uno
2.	OpenCM9.04 Board
3.	Dynamixel AX12 Actuators
4.	If U2D2 adapter, also need the appropriate wires
5.	If Arduino Uno, need Arduino USB connector and 3 Male to Female jumper wires

**Step 1 Configuring the Actuators -** The actuators need to be set up so that they have IDs ranging from 1 to 8 and no set limits. This can be done by either using the U2D2 adapter or an Arduino Uno. For each method please refer to the following documents:

* **U2D2 adapter**: “How to use the U2D2 adapter with Dynamixel Wizard 2.0 and DynamixelSDK”
* **Arduino Uno**: “Guide to Dynamixel AX-12A servos”

Step 2 Configuring OpenCM board - Install Arduino and setup Robotis OpenCM9.04 board support (refer to [OpenCM 9.04 e-manual](https://emanual.robotis.com/docs/en/parts/controller/opencm904/) 8.3. Arduino IDE) , and then upload the OpenCM9.04 firmware from ant11_cmd_dxl folder in this GitHub.


