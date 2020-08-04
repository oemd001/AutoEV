//Necessary package to run Ultrasonic Sensors. Might have to import it if not using on Kenneth's laptop. 
#include <NewPing.h>

//Sensor Pin Setup
const int BACK_ECHO = 2;
const int BACK_TRIG = 3;
const int FRONT_ECHO = 4;
const int FRONT_TRIG = 5;
const int RIGHT_ECHO = 6;
const int RIGHT_TRIG = 7;
const int LEFT_ECHO = 8;
const int LEFT_TRIG = 9;

//Motor Pin Setup
const int LEFT_MOTOR = 12;
const int RIGHT_MOTOR = 13;

int distance = 30;

void setup() {
  //Init output/input pins
  pinMode(BACK_ECHO, OUTPUT);
  pinMode(BACK_TRIG, OUTPUT);
  pinMode(FRONT_ECHO, OUTPUT);
  pinMode(FRONT_TRIG, OUTPUT);
  pinMode(RIGHT_ECHO, OUTPUT);
  pinMode(RIGHT_TRIG, OUTPUT);
  pinMode(LEFT_ECHO, OUTPUT);
  pinMode(LEFT_TRIG, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:


}
