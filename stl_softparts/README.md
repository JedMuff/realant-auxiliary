# Some Details About Soft Parts
*For details on suggested settings to use please refer to the parts catalog (**realant-auxiliary/docs/parts_catalogue.pdf**).These settings produced suitably soft parts, as with a higher infill density was too rigid for dampening.* 

*3D printers used were either the Ultimaker S3 or S5.*

*For details about how to attach the soft parts please refer to steps 1.1 and 6.1 of the construction documentation (**realant-auxiliary/docs/construction.md**).*

The regular legs of the Real-Ant robot are reasonably fit for their intended use. However one issue identified stems from the robot's primary use: reinforcement learning. This use case makes the Real-Ant likely to make more erratic motions and even slam itself to the ground. These motions might cause some durability problems for the robot such as screws coming loose.

One solution is using thread locking fluid. The thread locking fluid only solves the issue by fastening the screws, but it does not remove the shocks caused by the robot moving. Another solution was to change the design of the robot to incorporate soft parts.

## Designs
It was observed that the soft parts needed to be situated at the bottom of the leg and the bottom plate. The soft parts at the bottom plate are required because the
robot can strike the ground with its body first. 

Several designs for both the leg and the body plates were tested before these designs where settled upon. 

The leg piece simply substitutes soft filiment where necessary.
![softleg](/media/images/softleg.png)

The body plate protenction is in the form of simple soft tubes attached to the actuator connector with metal wire.
![fixdamper_4](/media/images/fixdamper_4.png)

# Copyright and License

leg.stl - Copyright (c) 2020 with Ote Robotics Ltd and Aalto University. Under MIT license. Copyright (c) 2023 Jed Muff, Eric Hannus, Antti Sippola, Julius Mikala, Jere Vespä. Under MIT license.

leg_damper.stl, round_joint_damper.stl - Copyright (c) 2023 Jed Muff, Eric Hannus, Antti Sippola, Julius Mikala, Jere Vespä. Under MIT license.

See LICENSE for details.