#include <LedControl.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 11
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
float Tfloat;
int Tint;
int redpin = 6;
int greenpin = 5;
int bluepin = 3;
LedControl lc=LedControl(8,10,9,1); 
// Pin 8->DIN, 10->CLK, 9->CS(LOAD), 1 = No.of devices
void show2digit(int num)
{
  int seg1,seg2;
    seg1 = num%10;
    seg2 = num/10;
    lc.setDigit(0,0,seg1,false); 
    if (num>=10)
          lc.setDigit(0,1,seg2,false);
    delay(300);
}
void setup(void)
{
    sensors.begin();
    lc.shutdown(0,false);  
    lc.setIntensity(0,5); 
    lc.clearDisplay(0);
    pinMode(redpin,OUTPUT);
    pinMode(greenpin,OUTPUT);
    pinMode(bluepin,OUTPUT);
} 
void loop(void)
{
    sensors.requestTemperatures(); 
    Tfloat = sensors.getTempCByIndex(0);
  if (Tfloat < 30)
  {
      Tint = int(Tfloat);
      lc.clearDisplay(0);
      show2digit(Tint);
      analogWrite(redpin,0);
      analogWrite(greenpin,255);
      analogWrite(bluepin,255);
  }
  if (Tfloat>= 30)
  {
    Tint = int(Tfloat);
    lc.clearDisplay(0);
    show2digit(Tint);
    analogWrite(redpin,255);
    analogWrite(greenpin,0);
    analogWrite(bluepin,0);
  }
}