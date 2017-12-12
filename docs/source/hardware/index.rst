
===============
Setting Up the Hardware
===============

Gripper robot was designed with microprocessor `Raspberry Pi version 3 <https://www.raspberrypi.org/>`_
. 
You will find a guide to setting up the hardware: Raspberry Pi and circuit schematic.

Raspberry
===============

***************
SDCard Image
***************
The OS version used on Raspberry Pi 3 is Ubuntu MATE 16.04.2.
The ROS version is Kinetic Kame. Kinetic was released early last year and is compatible with `Ubuntu Mate 16.04 <https://ubuntu-mate.org/raspberry-pi/>`_
. 

- Download `Ubuntu Mate image <https://ubuntu-mate.org/download/>`_ for raspiberry 2/3 - Version 16.04 (Xenial)
- Use `Etcher <https://etcher.io/>`_ to burn the image to SD cards & USB drives, safely and easily
- Image ready, let's install ROS!

***************
Install ROS
***************
The first step in installing ROS on Raspberry Pi 3 is :  
- Followed the steps on the download page, and within minutes I managed to have a Pi 3 running Ubuntu Mate.

- **Step 1:** Go to System -> Administration -> Software & Updates
- **Step 2:** Check the checkboxes to repositories to allow “restricted,” “universe,” and “multiverse.”
- **Step 3:** Setup your sources.list


- show fritzing schematics to connect the sensors, power, other boards, etc 



Bill of Materials
------------

- list here the parts requires to build your gripper. place links where to buy each part
- estimate the amout of PLA required for 3D printing
- estimate the cost to build a gripper

Building the Gripper 
------------

.. toctree::

   Printing the Gripper <3d-building>
   The Electronics  <pcbr