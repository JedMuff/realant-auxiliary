# Documentation Notes
This folder contains the following files:

- **U2d2_adapter_guide.md:** A guide on how to use the U2D2 adapter with Dynamixel Wizard 2.0 and DynamixelSDK. Used for configuring the actuators.
- **construction.md:** A step by step guide with images on how to make the robot. Also contains parts list.
- **construction.png:** An abstracted diagram showing the construction process.
- **dynamixel_A12A_guide.md:** A guide describing how the Dynamixel AX-12A servos work and how to configure them with the OpenCM board (not nessasary if using the U2d2_adapter).
- **parts_catalog.pdf:** A table showing the 3D printed parts and the setting used.
- **wiring_diagram.png:** Overall wiring diagram of the robot. The order of wiring on the boards does not matter. The ID numbers for the actuators does matter depending on the code that is used. The diagram shows what was used, with the front right actuators being 1 at the top and 2 at the bottom. This ID orientation was used to allow for easy visualization of the actuators when testing.

## Description of the Robot
The robot consists of a cover and base plates, to protect and structure the robot and legs for the robot to walk on. Both plates and leg parts are made with a 3D printer. The robot utilizes eight Dynamixel AX-12A servos for movements, two in each leg, and has eight degrees of freedom. 

Movements are sent by the Arduino based OpenCM9.04 control board and powered by a SMPS2Dynamixel power supply connector. The robot is controlled by a computer with a serial connection via USB cable using python scripts. A visual orientation tracker can be added on top of the robot's cover plate.