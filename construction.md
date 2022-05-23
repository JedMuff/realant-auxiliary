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

**Step 2 Configuring OpenCM board** - Install Arduino and setup Robotis OpenCM9.04 board support (refer to [OpenCM 9.04 e-manual](https://emanual.robotis.com/docs/en/parts/controller/opencm904/) 8.3. Arduino IDE) , and then upload the OpenCM9.04 firmware from ant11_cmd_dxl folder in this GitHub.

# Construction
## Parts Needed
1.	OpenCM9.04 Board
2.	Dynamixel AX12 Actuators (x8)
3.	Dynamixel AX12 Screws (that come with Dynamixel AX12s)
4.	Dynamixel AX12 support frames (that come with Dynamixel AX12s)
5.	Dynamixel AX/MX series (TTL) wire (x9)
6.	3D printed leg (x4) – Standard or soft version
7.	3D printed leg spacer (x4)
8.	3D printed Bottom body Plate
9.	3D printed Top Body plate
10.	SMPS2Dynamixel Board
11.	10mm M4 screws (x4)
12.	10mm M3 screws (x2)

## Optional Parts
1.	Steel wire
2.	Joint damper (x4)
3.	3D printed lid
4.	10 mm M4 screw
5.	M4 Nut
6.	3D printed stand
7.	10 mm M3 screw
![Parts](/media/images/parts.png)

**Step 1 Priming the Legs** - The leg spacers need to be attached to the legs. To do this you may need to sand down the grooves in the leg and use a mallet to push the spacer into place. Don't apply too much force however as it may break the print. A smooth connection between the two needs to be ensured so that there is enough space to slide onto the actuator. This is done for all 4 legs.
![Parts](/media/images/primingLegs.png)

**Step 1.1 (Optional) Fixing the soft Legs** - If you have opted for the soft legs, this is where the attachments are fitted on. This is simply done by sliding it onto the leg.
![Parts](/media/images/softleg.png)

**Step 2 Priming the OpenCM Board** - Solder on the TTL headers (x4 all facing the same direction) onto the OpenCM Board.
![Parts](/media/images/primingOpenCM.png)

**Step 3 Priming the SMPS2Dynamixel Board** - The SMPS2Dynamixel Board is prepared by cutting small holes in the film where 2 screw holes are. It is the two screw holes closest to the power connector. These holes are needed for mounting the board.
![Parts](/media/images/primingSMPS.png)

**Step 4 Attaching the Legs to the Actuators** - The legs are attached to the actuators through friction. The legs should slide onto the actuators with a bit of force. If the grip seems too loose, then screws can be used to add more friction. This is done for all 4 legs.
![Parts](/media/images/leg2Actuator.png)

**Step 5 Connecting the Support Frames** - Support frames are provided with the AX12's, along with screws. These first need to be connected with screws and bolts, 4 for each 2 supports for 1 leg. 16 screws and bolts are used overall for each leg.

![Parts](/media/images/supportframes.png)

**Step 6 Final Construction of the Leg** - Next the support frames are connected to the actuators, this is done once again with screws. Each connection requires 1 bigger screw and washer on one side and 4 smaller screws on the other. This is done for all 4 legs.

![Parts](/media/images/leg.png)

**Step 6.1 (Optional) Fixing the Dampers** - 
1. Fit the joint damper to a piece of steel wire and push the wire through the holes in the plastic frame:
![Parts](/media/images/fixdamper_1.png)
1. Push the wire through and tighten it from the inside of the frame by twisting the steel wire:
![Parts](/media/images/fixdamper_2.png)
3. Cut off any excess length of steel wire so it does not interfere with the joint movement, and finally re-attach the leg:
![Parts](/media/images/fixdamper_3.png)
4. Note that the wire cannot be routed through the slot in the frame piece closer to the body, as the joint damper is in the way. Route the wires through the slot in the other frame piece and try to keep the wire as tight as possible (while still allowing full motion of the joint!) near the body of the servo so that the wires do not drag under the robot:
![Parts](/media/images/fixdamper_4.png)
**Step 7 Fit the Bottom Plate** - The bottom plate is fitted by simply by screwing it in the top actuators with screws provided by the AX12's.
![Parts](/media/images/bottomPlate.jpg)
**Step 8 Fit the OpenCM Board** - The OpenCM board is fitted with 4 10mm M4 screws. To screw the board in a bit of force is required to drill into the 3D printed holes.
![Parts](/media/images/fitOpenCM.jpg)
**Step 9 Fit the SMPS2Dynamixel Board** - Next the SMPS2Dynamixel Board is fitted on top. Ensure it is facing the right direction and has the right orientation. Screw it in with 2 10mm M3 screws, it may require a bit of force to drill the screws into the drill holes.
![Parts](/media/images/fitSMPS.jpg)
**Step 10 Wire up the Robot** - Now the main structure is made, the wires can be connected in a neat orderly fashion. The Dynamixel AX-12A's are linked in a daisy chain fashion, it does not matter with port is used. One cable needs to be connected from the SMPS2Dynamixel board to the OpenCM Board, again it does not matter which port is used. Another cable is connected from the SMPS2Dynamixel board to an actuator (does not matter which as long as it is one at the top of the leg) and then all other top leg actuators are connected to the OpenCM board. 
![Parts](/media/images/wireup.png)

**Step 11 Fit the Top Plate** - The top plate is fitted by simply by screwing it in the top actuators with screws provided by AX12's.
![Parts](/media/images/topPlate.png)

**Step 12 (Optional) Adding the Lid** - The lid can be added by screwing it in with a 1 10 mm M4 screw and a M4 Nut.
![Parts](/media/images/lid.png)

**Step 13 (Optional) Adding the Stand** - The stand can be added using a 10 mm M3 screw, some force may be required to drill into the screw hole. The lid needs to be removed to perform this step.
![Parts](/media/images/stand.png)