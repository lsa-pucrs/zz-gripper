#include "Arduino.h" //needed for Serial.println
#include <PWMServo.h> 

//digital pins
#define servoRPin 10
#define servoLPin 9
#define trigPin 8 
#define echoPin 7 
#define pwmPin 6
#define dirPin 5
#define inputBPin 4
#define homePin 3
#define inputAPin 0 //interrupt 0 -> pin 2

//analogic pins
#define forceSensorPin 0
#define BAUDRATE 9600


//commandVariables
String readString; //para entrada serial
String commandName="";
int16_t commandValue=0;
boolean commandDone = false;

//gripperVariables
boolean gripperActive = true;
uint16_t gripperSpeedSetPoint = 50;
int16_t gripperPosition;
int16_t gripperPositionSetPoint;
int8_t gripperMode = 0; //0 open/ 1 close/ 2 auto
int8_t lastGripperMode = 1;
PWMServo gpp_R;  
PWMServo gpp_L; 
boolean gripperState = false;
//Right 45 min, 60 mid, 150 max 
int16_t gpp_RMax = 136;///160;
int16_t gpp_RMin = 55;
//Left 145 min, 120 mid, 50 max
int16_t gpp_LMax = 34; //30
int16_t gpp_LMin = 120;
//////////////////////////
int16_t gpp_RPos = gpp_RMin;
int16_t gpp_LPos = gpp_LMin;

//sonar
uint8_t gripperDistance;
uint8_t gripperDistanceSetPoint = 15;
boolean sonarActive = false;
boolean sonarFlag = false; //when it found something

//forceSensor
uint16_t gripperForce;
uint16_t gripperForceSetPoint = 50; //hard 0; easy 1024; to activate

//encoder
int16_t ITerm1 = 0, ITerm2 = 0;
int16_t ComposedSetPoint;
int16_t gripperRotationXSetPoint;
volatile int16_t gripperRotationX = 0;
volatile boolean inputB = false;
double n = 0;
double pwmValue = 0;

//general
int val;
unsigned long time;
unsigned long lastTime;
unsigned long lastTimeCloseDelay;
unsigned long lastTimeRotationDelay;
unsigned long lastTimeSpinOnce;

///////////////////////////////////////////////////////////////////////////////
//FUNCTIONS DECLARATIONS 
///////////////////////////////////////////////////////////////////////////////
void computeCommand(String rawInput);
void updateGripperActions();
void helpToPrint();
boolean close();
boolean close(int newPos);
boolean close(uint16_t newPos,uint16_t newSpeed);
boolean open();
boolean closeRoutine();
void computeEncoderX(int16_t setPoint);
void homeRoutine();
uint8_t measureDistance();

///////////////////////////////////////////////////////////////////////////////
//MAIN FUNCTION
///////////////////////////////////////////////////////////////////////////////
void computeCommand(String rawInput){
  String auxName = "";
  int16_t auxValue = 0;
  int firstCharIndex = rawInput.indexOf('_');
  if(firstCharIndex<0) firstCharIndex = rawInput.indexOf(' '); //multiplos comandos
  if(firstCharIndex>0){
    String numberCommand = "";
    for(int i = firstCharIndex+1; i < rawInput.length(); i++){ //se rawInput.length()-1 nao le a ultima string
      numberCommand += rawInput[i];
    }
    auxValue = numberCommand.toInt();
    for(int i = 0; i < firstCharIndex; i++){
      auxName+=rawInput[i];
    }
  }
  else{ //if index <= 0
    auxValue = rawInput.toInt();
    auxName = rawInput; 
  }
  if(commandValue!=auxValue||commandName!=auxName){
    commandDone=false;
    commandValue=auxValue;
    commandName=auxName;
  }
}

void updateGripperActions(){
  if(commandName=="help")helpToPrint();
  else if(commandName=="close"){
    if(commandValue==101){
      if(sonarFlag)sonarActive = false;
      else sonarActive = true;
      close();
    }
    else close(commandValue);
  }
  else if(commandName=="open"){
    sonarFlag = false; //para resetar sonar na closeRoutine()
    open();
  }
  else if(commandName=="setForce")gripperForceSetPoint = commandValue;
  else if(commandName=="setSpeed")gripperSpeedSetPoint = commandValue;
  else if(commandName=="setDistance")gripperDistanceSetPoint = commandValue;
  else if(commandName=="rotate")gripperRotationXSetPoint = commandValue;
  else if(commandName=="home")homeRoutine();
  //else rosPrint("Unknown command!");
}


/*void rosPrint(char message){
  std_msgs::String msg;
  msg.data = message;
  nh.loginfo(msg.data);
  //nh.loginfo("msg");
}*/

void helpToPrint(){}

boolean close(){return close(100);}
boolean close(int newPos){return close(newPos,gripperSpeedSetPoint);}
boolean close(uint16_t newPos,uint16_t newSpeed){
  if(closeRoutine()){
    int16_t setPointR = map(newPos,0,100,gpp_RMin,gpp_RMax);
    int16_t setPointL = map(newPos,0,100,gpp_LMin,gpp_LMax);
    time = millis();
    unsigned long closeDelay = time - lastTimeCloseDelay;
    if(closeDelay >= newSpeed){ 
      lastTimeCloseDelay = time;
      if(gpp_RPos<setPointR)gpp_RPos+=1; //close R
      if(gpp_RPos>setPointR)gpp_RPos-=1; //open R
      if(gpp_LPos>setPointL)gpp_LPos-=1; //close L
      if(gpp_LPos<setPointL)gpp_LPos+=1; //open L 
      gpp_R.write(gpp_RPos);
      gpp_L.write(gpp_LPos); 
      return true;
    }
    
  }
  return false;
}

boolean open(){
  gpp_RPos = gpp_RMin;
  gpp_LPos = gpp_LMin;
  gpp_R.write(gpp_RPos); //45 min, 60 mid, 150 max  
  gpp_L.write(gpp_LPos);//145 min, 120 mid, 50 max
}

boolean closeRoutine(){
  gripperForce = analogRead(forceSensorPin);//map(gripperForce,0,111,1023,0); //4.2v = 111N = 11.34kg
  if(gripperForce>gripperForceSetPoint)return false; 

  if(sonarActive){
    gripperDistance = measureDistance();
    if(gripperDistance>gripperDistanceSetPoint)return false;
    else sonarFlag = true;
  }
  return true;
}

void computeEncoderX(int16_t setPoint){
  int16_t input = gripperRotationX; 
  int16_t erro = input - (-1*setPoint); // -1* inverte rotacao
  int16_t erro1 = map(erro,0,600,0,-255); //255 é o valor maximo do pwm
  int16_t erro2 = map(erro,0,600,0,255); // 600 pulsos, é o angulo max (90°)
  float kp=10;
  int16_t output1 = kp*erro1;
  int16_t output2 = kp*erro2;
  if(output1>255)output1=255;
  else if(output2>255)output2=255;
  if(output1<0)output1=0; //120 -> pwm minimo para mover a garra
  else if(output2<0)output2=0;

  analogWrite(dirPin,output1);
  analogWrite(pwmPin,output2); //0   
}

void homeRoutine(){
  open();
  gripperRotationX = 0;
  uint16_t homePos = 0;
  while(!digitalRead(homePin)){
    homePos--;
    computeEncoderX(homePos);
    delay(5);
  }
  gripperRotationX = 0;
  gripperRotationXSetPoint=450;
}

/*
void homeRoutine(){
  open();
  uint16_t homePos = 0;
  while(!digitalRead(homePin)){
    homePos--;
    computeEncoderX(homePos);
    delay(5);
  }
  homePos = 0;
  gripperRotationX = 0;
  gripperRotationXSetPoint=450;

  while(homePos<450){
    homePos++;
    computeEncoderX(homePos);
    delay(5);
  }
}*/

uint8_t measureDistance()
{
  uint8_t maximumRange = 200; // Maximum range needed
  uint8_t minimumRange = 0; // Minimum range needed
  uint16_t duration; 
  uint8_t distance; // Duration used to calculate distance
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  /* The following trigPin/echoPin cycle is used to determine the
  distance of the nearest object by bouncing soundwaves off of it. */ 
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2); 
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10); 
   
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
   
  //Calculate the distance (in cm) based on the speed of sound.
  distance = duration/58.2; //g
   
  if (distance >= maximumRange || distance <= minimumRange){
  ///* Send a negative number to computer to indicate "out of range" */
    return 0;
  }
  else return distance;//g
}

