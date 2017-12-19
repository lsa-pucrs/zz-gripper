
=============================================
Installing ROS
=============================================


About ROS
-----------------------------


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

.. code-block:: bash

	sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'


- **Step 4:** Setup your keys

.. code-block:: bash

		wget http://packages.ros.org/ros.key -O - | sudo apt-key add -


- **Step 5:** To be sure that your Ubuntu Mate package index is up to date, type the following 

.. code-block:: bash

		sudo apt-get update

- **Step 6:** Install ros-kinetic-desktop-full
	.. code-block:: bash

		sudo apt-get install ros-kinetic-desktop-full

- **Step 7:** Initialize rosdep
	.. code-block:: bash

		sudo rosdep init
		rosdep update

- **Step 8:** Setting up the ROS environment variables
	.. code-block:: bash

		echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
		source ~/.bashrc

- **Step 9:** Create and initialize the catkin workspace
	.. code-block:: bash

		sudo apt-get update
		mkdir -p ~/catkin_workspace/src
		cd catkin_workspace/src
		catkin_init_workspace
		cd ~/catkin_workspace/
		catkin_make

- **Step 10:** Add the catkin_workspace to your ROS environment
	.. code-block:: bash
		source ~/catkin_workspace/devel/setup.bash
		echo “source ~/catkin_workspace/devel/setup.bash” >> ~/.bashrc

- **Step 11:** Check the ROS environment variables

		.. code-block:: bash
			export | grep ROS

