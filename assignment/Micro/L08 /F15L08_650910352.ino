int motorPin = 9;
char command;

void setup() {
  Serial.begin(9600);
  pinMode(motorPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.read();
    if (command == 'a') {
      digitalWrite(motorPin, LOW); 
    } else if (command == 'b') {
      digitalWrite(motorPin, HIGH); 
    }
  }
}
