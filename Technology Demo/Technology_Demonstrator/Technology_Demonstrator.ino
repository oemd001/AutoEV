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

//Sensor detection variables
//Back Sensor Variables
double bdistance;
double bduration;
//Front Sensor Variables
double fdistance;
double fduration;
//Left Sensor Variables
double ldistance;
double lduration;
//Right Sensor Variables
double rdistance;
double rduration;

//debug LED
int ledPin = 13;

void setup() {
  //Init output/input pins
  Serial.begin(9600);
  pinMode(BACK_ECHO, INPUT);
  pinMode(BACK_TRIG, OUTPUT);
  pinMode(FRONT_ECHO, INPUT);
  pinMode(FRONT_TRIG, OUTPUT);
  pinMode(RIGHT_ECHO, INPUT);
  pinMode(RIGHT_TRIG, OUTPUT);
  pinMode(LEFT_ECHO, INPUT);
  pinMode(LEFT_TRIG, OUTPUT);
}

void loop() {
  //back facing UltraSonic sensor loop
  //digitalWrite(ledPin, LOW);
  digitalWrite(BACK_TRIG, HIGH);
  delay(50);
  digitalWrite(BACK_TRIG, LOW);
  bduration = pulseIn(BACK_ECHO, HIGH);
  bdistance = (bduration/2)/29.1;
  if (bdistance <= 10) {
    //digitalWrite(ledPin, HIGH);
    delay(50);
    Serial.println("Obstacle detected @ back ");
    Serial.println(bdistance);
    Serial.println("cm");
  }

  //forward facing UltraSonic sensor loop
  digitalWrite(FRONT_TRIG, HIGH);
  delay(50);
  digitalWrite(FRONT_TRIG, LOW);
  fduration = pulseIn(FRONT_ECHO, HIGH);
  fdistance = (fduration/2)/29.1;
  if (fdistance <= 10) {
    //digitalWrite(ledPin, HIGH);
    delay(50);
    Serial.println("Obstacle detected @ front ");
    Serial.println(fdistance);
    Serial.println("cm");
  }

  //Left facing Ultrasonic sensor loop
  digitalWrite(LEFT_TRIG, HIGH);
  delay(50);
  digitalWrite(LEFT_TRIG, LOW);
  lduration = pulseIn(LEFT_ECHO, HIGH);
  ldistance = (lduration/2)/29.1;
  if (ldistance <= 10) {
    //digitalWrite(ledPin, HIGH);
    delay(50);
    Serial.println("Obstacle detected @ left ");
    Serial.println(ldistance);
    Serial.println("cm");
  }

  //Right facing Ultrasonic sensor loop
  digitalWrite(RIGHT_TRIG, HIGH);
  delay(50);
  digitalWrite(RIGHT_TRIG, LOW);
  rduration = pulseIn(RIGHT_ECHO, HIGH);
  rdistance = (rduration/2)/29.1;
  if (rdistance <= 10) {
    //digitalWrite(ledPin, HIGH);
    delay(50);
    Serial.println("Obstacle detected @ right ");
    Serial.println(rdistance);
    Serial.println("cm");
  }
  
  
}
