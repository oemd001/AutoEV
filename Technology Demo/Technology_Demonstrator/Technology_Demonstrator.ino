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
  /* Here, the code should include DC motor constantly running
   * UNTIL one of the 'if' conditions are met. 
   */


  
  //back facing UltraSonic sensor loop
  digitalWrite(BACK_TRIG, HIGH);
  delay(50);
  digitalWrite(BACK_TRIG, LOW);
  bduration = pulseIn(BACK_ECHO, HIGH);
  bdistance = (bduration/2)/29.1;
  if (bdistance <= 10) {
    delay(50);
    Serial.println("Obstacle detected @ back ");
    Serial.println(bdistance);
    Serial.println("cm");
    // Here, if bdistance is less than 10, the motor should run forward @ 1/4 speed for 5s and exit loop. 
  }

  //forward facing UltraSonic sensor loop
  digitalWrite(FRONT_TRIG, HIGH);
  delay(50);
  digitalWrite(FRONT_TRIG, LOW);
  fduration = pulseIn(FRONT_ECHO, HIGH);
  fdistance = (fduration/2)/29.1;
  if (fdistance <= 10) {
    delay(50);
    Serial.println("Obstacle detected @ front ");
    Serial.println(fdistance);
    Serial.println("cm");
    //Here, if the obstacle is detected at the front, the entire car should stop for delay(100)

    while (fdistance <= 15) {
      digitalWrite(FRONT_TRIG, HIGH);
      delay(50);
      digitalWrite(FRONT_TRIG, LOW);
      fduration = pulseIn(FRONT_ECHO, HIGH);
      fdistance = (fduration/2)/29.1;
      //Serial.println is optional here. 
      Serial.println("reversing... ");
      delay(100);
      Serial.print(fdistance);
      /* Given that the obstacle is detected at the front, the car should reverse at 1/4 speed. for 1.5s
       * The car must then first turn clockwise for 3s. If fdistance is still <= 15, it will revert itself to origin by turning counterclockwise for 3s.
       * The car will then turn counterclockwise for 3s, or when fdistance is no longer <= 15–whichever comes first. 
       * necessary logic: while loop
       */
       
    }
  }

  //Left facing Ultrasonic sensor loop
  digitalWrite(LEFT_TRIG, HIGH);
  delay(50);
  digitalWrite(LEFT_TRIG, LOW);
  lduration = pulseIn(LEFT_ECHO, HIGH);
  ldistance = (lduration/2)/29.1;
  if (ldistance <= 10) {
    delay(50);
    Serial.println("Obstacle detected @ left ");
    Serial.println(ldistance);
    Serial.println("cm");
    /* 
     * If this condition is true, entire car should delay(100);
     * The car will turn counterclockwise until either fdistance is not <= 10 and rdistance is not <=10
     * OR the motor has spun it's wheels for 10 seconds at 1/4 power. (right motor HIGH, left motor -HIGH). (counterclockwise)
     * If latter condition continues, fdistance and ldistance must sense an object. The condition must stop when fdistance no longer senses an object. 
     * Necessary logic: while loop
     */
  }

  //Right facing Ultrasonic sensor loop
  digitalWrite(RIGHT_TRIG, HIGH);
  delay(50);
  digitalWrite(RIGHT_TRIG, LOW);
  rduration = pulseIn(RIGHT_ECHO, HIGH);
  rdistance = (rduration/2)/29.1;
  if (rdistance <= 10) {
    delay(50);
    Serial.println("Obstacle detected @ right ");
    Serial.println(rdistance);
    Serial.println("cm");

    /*
     * Similar logic to left facing ultrasonic sensor loop. 
     * As opposed to being counterclockwise, it is clockwise. (right motor -HIGH, left motor HIGH)
     * Necessary logic: while loop
     */
  }
  
  
}
