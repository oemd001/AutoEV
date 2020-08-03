const int pin1 = 2;
const int pin2 = 3;

void setup() {
  // put your setup code here, to run once
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(pin1, HIGH);
  digitalWrite(pin2, HIGH);
}
