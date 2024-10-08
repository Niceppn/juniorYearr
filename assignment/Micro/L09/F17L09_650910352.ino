#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>

SoftwareSerial mySerial(10, 11);
DFRobotDFPlayerMini myDFPlayer;

const int buttonPins[] = {2, 3, 4, 5, 6};
const int soundFiles[] = {1, 2, 3, 4, 5};

void setup() {
  mySerial.begin(9600);
  Serial.begin(9600);
  
  for (int i = 0; i < 5; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }

  if (!myDFPlayer.begin(mySerial)) {
    while (true);
  }
}

void loop() {
  for (int i = 0; i < 5; i++) {
    if (digitalRead(buttonPins[i]) == LOW) {
      myDFPlayer.play(soundFiles[i]);
      delay(1000);
      while (digitalRead(buttonPins[i]) == LOW);
    }
  }
}
