RealAnt Auxiliary
=================
![robot_transparent](/media/images/robot_transparent.png)
The RealAnt Auxiliary contains additioning documentation, improved designs and some simple walk gait code for the RealAnt designed by Ote Robotics at Aalto University (https://github.com/OteRobotics/realant).

The repository provides improvements relating to robustness and usability. These are related to the screw fittings and the repairability of the design. Design improvements included:
1. soft attachments to dampen damage to the robot (see 'stl_softparts' folder)
2. proper board mounting for easy construction (see 'stl_standard' folder)
3. access hatches for ease of use and repairability (see 'stl_standard' folder)
4. a stand for a motion tracking marker(used inreinforcement learning) (see 'stl_standard' folder)

Additionally with an improved robot design, some code was developed that utilized DYNAMIXEL AX-12A actuators to produce walking gaits and gestures the quadruped robot could use for initial functionality testing (see 'code' folder). 

Watch the youtube video here: https://www.youtube.com/watch?v=h07QOblhzB0.

![product](/media/images/product.png)

More detailed documentation on contruction and usage where made, this can be found in the **docs** folder. 

# Structure of the GitHub
The key folders in this repository are described below, see the README kept in each directory for more details:

- **code:** Contains all the code needed for running the robot, including some simple gaits for testing.
- **docs:** Contains all the documentation for constructing and using the robot.
- **media:** Some images used in the documentation with some additional bonus images of the robot. Also contains a video made about the project. 
- **stl_softparts:** Contains the soft parts made.
- **stl_standard:** Contains the improved parts made. A modified spacer was added that improves the fit to the leg.

# Get in Contact
If you want to contribute to this repo or need any help these are the people to contact.
* Jed Muff - GitHub Managment and general help (https://www.linkedin.com/in/jed-muff/) 
* Eric Hannus - Working with the code (https://www.linkedin.com/in/eric-hannus/)
* Antti Sippola - Standard 3D printed parts (https://www.linkedin.com/in/anttisippola/)
* Julius Mikala - Soft 3D printed parts (https://www.linkedin.com/in/julius-mikala-594791178/)
# Links
**RealAnt (developed by Ote Robtics) GitHub:** https://github.com/OteRobotics/realant

**Reinforcement Learning with RealAnt** – https://github.com/AaltoVision/realant-rl

**RealAnt Auxiliary GitHub:** https://github.com/JedMuff/realant-auxiliary

**Intelligent Robotics Research Group Webpage:** https://irobotics.aalto.fi/ 

**Wiki page:** https://wiki.aalto.fi/display/AEEproject/Building+a+quadruped+robot+for+reinforcement+learning+research

**Research group page about this project:** https://irobotics.aalto.fi/building-a-quadruped-robot/

# Resources
**AX12A - EManual:** https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/

**AX12 - Usermanual:** https://www.crustcrawler.com/products/bioloid/docs/AX-12.pdf

**OpenCM 9.04 - EManual:** https://emanual.robotis.com/docs/en/parts/controller/opencm904/

**Credits**:
Jed Muff, Jere Vepsä, Eric Hannus, Antti Sippola, Julius Mikala, Rituraj Kaushik, Ote Robotics

# Copyright and License

The files in this repository share files with the original [RealAnt](https://github.com/OteRobotics/realant) repository. As such the repository shares Copyright (c) 2020 with Ote Robotics Ltd and Aalto University and is licensed under MIT license. To the best of our ability we have labelled which files belong under the Ote Robotics Ltd license and which files come under the authors of this repository Copyright (c) 2023 Jed Muff, Eric Hannus, Antti Sippola, Julius Mikala, Jere Vespä.

See LICENSE for details.