#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>

SoftwareSerial mySerial(10, 11);
DFRobotDFPlayerMini myDFPlayer;

const int flameSensorPin = 2;

void setup() {
  mySerial.begin(9600);
  Serial.begin(9600);
  pinMode(flameSensorPin, INPUT);

  if (!myDFPlayer.begin(mySerial)) {
    while (true);
  }
}

void loop() {
  if (digitalRead(flameSensorPin) == HIGH) {
    myDFPlayer.play(1);
    delay(10000);
  }
}
