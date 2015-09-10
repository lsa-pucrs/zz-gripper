## Instalation guide

  $sudo apt-get install ros-hydro-rosserial-arduino  
  $sudo apt-get install ros-hydro-teleop-twist-keyboard  
  $cd ~/catkin_ws/src/  
  $git clone https://github.com/lsa-pucrs/zz-gripper -b hydro-devel  
  $cd ~/catkin_ws/  
  $catkin_make_isolated  
  $source ~/catkin_ws/devel/setup.bash  

## Usage guide

### How to launch the driver 
  $sudo chmod 666 /dev/ttyUSB0  
  $roslaunch zz_gripper teleop.launch 
  
#### Subscribed Topics
   /gripperCommands
   Obs: The keys will send strings to the  topic and can be used in the same time that rostopic publishs.

#### Published Topics  
  
  
### How to send commands via the terminal
  $rostopic pub -1 /gripperCommands std_msgs/String "close_50"  
  Obs: To send a command from the code, just publish an string message in the /gripperCommands one of the following commands  

#### Command list:
  - close_101     :close when sonar detects an object at the set distance  
  - close_X       : X ranges from 0 to 100. 0 is open and 100 is closed  
  - setForce_X    :default 50 (strong 0; weak 1024)  
  - setSpeed_X    :default 50   
  - setDistance_X :default 15(cm) (min 2, max 200)  
  - rotate_X      :middle 550 (gripper_up 100, gripper_down 700)  
  - home          :Defines the initial position  
  - open          :Gripper Open  

### How to send commands via the GUI application


### How to send commands via keyboard

