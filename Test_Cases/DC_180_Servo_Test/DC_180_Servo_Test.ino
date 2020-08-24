#include <Servo.h>

/* READ THIS BEFORE USING THIS PROGRAM
 * Hello, if we're using an oscillation method to scan for objects, DO NOT USE the SG90 servo. 
 * For some reason, oscillation only works between the following ranges: 0° to 135°. <- NO CLUE WHY
 * Also, it doesn't like for loops either. 
 * Finally, if we have no choice but to use this servo, I'm inheriting this program to our main() program. 
 */
const int pwm = 2;
const int LIMIT = 180;
const int MIN = 0;
int pos = 0; //moving pos of servo from 0 to 180

Servo servo; //init servo object/class

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //When using serial mon, set baud rate to 9600
  servo.attach(2); //init servo to pin 2
}

void loop() {
  // put your main code here, to run repeatedly:

  //Inefficient way to run this but that's the only way I was able to get it running. (3AM)
   servo.write(0);
   delay(1000);
   servo.write(45);      
   delay(1000);          
   servo.write(90);      
   delay(1000);          
   servo.write(135);     
   delay(1000);
   servo.write(180);
   delay(1000);
   servo.write(135);
   delay(1000);          
   servo.write(90);      
   delay(1000);
   servo.write(45);
   delay(1000);
}
