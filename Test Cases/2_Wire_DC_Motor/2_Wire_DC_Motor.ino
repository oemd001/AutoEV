/*  README FIRST!
 *  Prior to running this program, you must have the following:
 *  2x PN2222 Transistor
 *  1x 1N4001 diode
 *  1x 270 Ω Resistor
 *  Without these materials, the DC motor will not work when plugged in to it's designated pin. 
 *  HOWEVER, it will run via 5V DC. 
 */

const int pin1 = 13; //right Motor
const int pin2 = 12; //left Motor

void setup() {
  // put your setup code here, to run once
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(pin1, HIGH);
  digitalWrite(pin2, HIGH); //Different orientations. 
}
