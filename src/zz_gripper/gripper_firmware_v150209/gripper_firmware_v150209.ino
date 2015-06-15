/*
Force Sensor A201-25 (0-25 lb. force range 111.205N) acessado em http://www.phidgets.com/documentation/Phidgets/3100_0_FlexiforceUserManual.pdf
Rotation Speed ~38.27rpm source: Motor Pololu 70:1 = 150RPM em 12v =  (((15.0/21)**2)*150)/2^= ~38.27

Servo mg996:
Velocidade de operação: 0.13sec / 60 graus (6.0V sem carga) = 0.174seg 80graus
Torque Stall: 15 kg-cm (208,3 oz-in) em 6V
*/
#include "gripper_firmware.h"
#include <PWMServo.h> //tem que estar no .h e no sketch
#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/UInt8.h>
#include <std_msgs/UInt16.h>
#include <std_msgs/Int16.h>



ros::NodeHandle nh;

void callCommand( const std_msgs::String& gripper_msg){
  readString=gripper_msg.data;
}

std_msgs::String status_msg;
std_msgs::UInt16 topicSpeed;
std_msgs::Int16 topicPosition;
std_msgs::UInt8 topicDistance;
std_msgs::UInt16 topicForce;
std_msgs::Int16 topicRotationX;

ros::Subscriber<std_msgs::String> subGripperCommands("gripperCommands" , callCommand);

ros::Publisher advGripperSpeed("gripperSpeed", &topicSpeed);
ros::Publisher advGripperForce("gripperForce", &topicForce);
ros::Publisher advGripperPosition("gripperPosition", &topicPosition);
ros::Publisher advGripperDistance("gripperDistance", &topicDistance);
ros::Publisher advGripperRotationX("gripperRotationX", &topicRotationX);

void setup()   {
  pinMode(dirPin,OUTPUT);
  pinMode(pwmPin,OUTPUT);
  pinMode(inputBPin,INPUT); //inputB // white wire
  pinMode(homePin,INPUT);
  attachInterrupt(inputAPin,incA,FALLING); //pin 2 inputA // yellow wire

  //gripper
  gpp_R.attach(servoRPin);  
  gpp_L.attach(servoLPin);
  //#gripper
  nh.initNode();
  nh.subscribe(subGripperCommands);
  nh.advertise(advGripperSpeed);
  nh.advertise(advGripperForce);
  nh.advertise(advGripperPosition);
  nh.advertise(advGripperDistance);
  nh.advertise(advGripperRotationX);

  nh.spinOnce();
  delay(50);
}



void loop(){
  //ROS PUBLISHERS
  topicForce.data = gripperForce;
  advGripperForce.publish(&topicForce);
  topicPosition.data = gripperPosition;
  advGripperPosition.publish(&topicPosition);
  topicRotationX.data = gripperRotationX;
  advGripperRotationX.publish(&topicRotationX);
  topicDistance.data = gripperDistance;
  advGripperDistance.publish(&topicDistance);

  //encoder dalay
  time = millis();
  unsigned long rotationDelay = time - lastTimeRotationDelay;
  if(rotationDelay >= gripperSpeedSetPoint/10){ // dividido por 10 pois, 5ms é o delay ideal dealy deafault: 50ms
    lastTimeRotationDelay = time;
    if(ComposedSetPoint<gripperRotationXSetPoint)ComposedSetPoint++;
    if(ComposedSetPoint>gripperRotationXSetPoint)ComposedSetPoint--;
    computeEncoderX(ComposedSetPoint);
  }


  //compute command delay
  time = millis();
  unsigned long wait = time - lastTime;  
  if(wait >= 100){ //amory: declarar como constante
    lastTime = time;
    computeCommand(readString);
    //gripperForce = analogRead(forceSensorPin);//map(gripperForce,0,111,1023,0); //4.2v = 111N = 11.34kg
    //gripperDistance = measureDistance();
    //gripperCurrent = analogRead(currentSensorPin);
  }

  updateGripperActions();

  unsigned long waitSpinOnce = time - lastTimeSpinOnce;  
  if(waitSpinOnce >= 50){ 
    lastTimeSpinOnce = time;
    nh.spinOnce(); //evitar delay pois afeta na movimentacao da gripper
  }
}

void incA(){
  inputB = digitalRead(inputBPin);
  if(inputB)gripperRotationX--;
  else gripperRotationX++;
}


