


=============================================
Installing ROS
=============================================


About ROS
-----------------------------

 - links to papers and manuals or other tutorials
 - 

How to install the driver and its depedencies
-----------------------------

***************
Install ROS
***************
The first step in installing ROS on Raspberry Pi 3 is :  
- Followed the steps on the download page, and within minutes I managed to have a Pi 3 running Ubuntu Mate.

- **Step 1:** Go to System -> Administration -> Software & Updates
- **Step 2:** Check the checkboxes to repositories to allow “restricted,” “universe,” and “multiverse.”
- **Step 3:** Setup your sources.list
*sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'*
- **Step 4:** Setup your keys
*wget http://packages.ros.org/ros.key -O - | sudo apt-key add -*
- **Step 5:** To be sure that your Ubuntu Mate package index is up to date, type the following command
*sudo apt-get update*
- **Step 6:** Install ros-kinetic-desktop-full
*sudo apt-get install ros-kinetic-desktop-full*
- **Step 7:** Initialize rosdep
*sudo rosdep init*
*rosdep update*
- **Step 8:** Setting up the ROS environment variables
*echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc*
*source ~/.bashrc*
- **Step 9:** Create and initialize the catkin workspace
*mkdir -p ~/catkin_workspace/src*
*cd catkin_workspace/src*
*catkin_init_workspace*
*cd ~/catkin_workspace/*
*catkin_make*
- **Step 10:** Add the catkin_workspace to your ROS environment
*source ~/catkin_workspace/devel/setup.bash*
*echo “source ~/catkin_workspace/devel/setup.bash” >> ~/.bashrc*
- **Step 11:** Check the ROS environment variables
*export | grep ROS*


- provide a script to install it all at once

Known limitations
-----------------------------

describe here any known limitation of the software so that the next student is aware of it.

How to test it
-----------------------------

- basic testing to see if the  is procedure working on the RPi

