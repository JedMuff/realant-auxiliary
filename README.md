TheRealestAnt
=======
![robot_transparent](/media/images/robot_transparent.png)
This repository contains additioning documentation, improved designs and some simple walk gait code for the Real-Ant designed by Ote Robotics at Aalto University. This GitHub page was made in conjunction with the "ELEC-E8004 Project Work" module and the Intelligent Robotics Research group at Aalto University. For this reason some of the documents found in this GitHub correspond to the requirements of the research group and the module. More details about the project are in the appendix folder.

With the RealAnt design, issues with robustness and usability were identified. These are related to the screw fittings and the repairability of the design. Design improvements included:
1. soft attachments to dampen damage to the robot (see 'stl_softparts' folder)
2. proper board mounting for easy construction (see 'stl_standard' folder)
3. access hatches for ease of use and repairability (see 'stl_standard' folder)
4. a stand for a motion tracking marker(used inreinforcement learning) (see 'stl_standard' folder)

![product](/media/images/product.png)
See also '/appendix/1-10_Final_report_E8004_2022_signed.pdf' results section for some more detailed documentation about the designs.

Additionally with an improved robot design, some code was developed that utilized DYNAMIXEL AX-12A actuators to produce walking gaits and gestures the quadruped robot could use for initial functionality testing (see 'code' folder). 

More detailed documentation on contruction and usage where made, this can be found in the docs folder. 

# Structure of the GitHub
The key folders in this repository are described below:

- **appendix:** Contains files made for the module. **'1-10_Final_report_E8004_2022_signed.pdf'** file gives a good overview of the project and some more detailed descriptions of the parts made.
- **archive:** Is a copy of the RealAnt repo at the current period of this project. Serves as a good reference and keeping the project whole. https://github.com/OteRobotics/realant 
- **code:** Contains all the code needed for running the robot, including some simple gaits for testing. The **README** contained within provides more details.
- **docs:** Contains all the documentation for constructing and using the robot. The **README** contained within provides more details.
- **media:** Some images used in the documentation with some additional bonus images of the robot. Also contains a video made about the project. 
- **stl_softparts:** Contains the soft parts made. See **docs** and **'1-10_Final_report_E8004_2022_signed.pdf'** results section for more details.
- **stl_standard:** Contains the improved parts made. A modified spacer was added that improves the fit to the leg. See **docs** and **'1-10_Final_report_E8004_2022_signed.pdf'** results section for more details on other parts.

# Links
**Intelligent Robotics Research Group Webpage:** https://irobotics.aalto.fi/ 

**RealAnt (developed by Ote Robtics) GitHub:** https://github.com/OteRobotics/realant

**TheRealestAnt GitHub:** https://github.com/JedMuff/TheRealestAnt

**Wiki page:** https://wiki.aalto.fi/display/AEEproject/Building+a+quadruped+robot+for+reinforcement+learning+research

**Research group page about this project:** https://irobotics.aalto.fi/building-a-quadruped-robot/

**Reinforcement Learning with RealAnt** – https://github.com/AaltoVision/realant-rl

# Resources
**AX12A - EManual:** https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/

**AX12 - Usermanual:** https://www.crustcrawler.com/products/bioloid/docs/AX-12.pdf

**OpenCM 9.04 - EManual:** https://emanual.robotis.com/docs/en/parts/controller/opencm904/
