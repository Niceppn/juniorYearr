int pirPin = 7;
int pirState = LOW;

void setup() {
  pinMode(pirPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  pirState = digitalRead(pirPin);
  
  if (pirState == HIGH) {
    Serial.println("motion_detected");
  } else {
    Serial.println("no_motion");
  }

  delay(1000);
}
