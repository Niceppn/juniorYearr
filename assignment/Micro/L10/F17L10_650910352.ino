const int vibrationPin = A0;

void setup() {
  Serial.begin(9600);
  pinMode(vibrationPin, INPUT);
}

void loop() {
  int vibrationValue = analogRead(vibrationPin);

  if (vibrationValue > 500) {
    Serial.println("Vibration Detected");
  } else {
    Serial.println("No Vibration");
  }

  delay(1000);
}
