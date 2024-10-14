int waterSensorPin = A0;
int waterLevel = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  waterLevel = analogRead(waterSensorPin);
  int waterPercentage = map(waterLevel, 0, 1023, 0, 100);
  
  Serial.println(waterPercentage);
  delay(1000);
}
