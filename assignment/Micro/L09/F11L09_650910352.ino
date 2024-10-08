#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>

SoftwareSerial mySerial(2, 3);
DFRobotDFPlayerMini myDFPlayer;

const int flameSensorPin = A0;
bool flameDetected = false;

void setup() {
    mySerial.begin(9600);
    Serial.begin(9600);
    if (!myDFPlayer.begin(mySerial)) {
        Serial.println("DFPlayer Mini not found");
        while (true);
    }
    myDFPlayer.volume(10);
}

void loop() {
    int sensorValue = analogRead(flameSensorPin);
    if (sensorValue > 300) { // เปลี่ยนค่า 300 ตามค่าที่เหมาะสม
        if (!flameDetected) {
            flameDetected = true;
            myDFPlayer.play(1); // เล่นเสียงที่ 1
        }
    } else {
        flameDetected = false;
    }
}
