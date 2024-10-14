#include <LiquidCrystal_I2C.h> 
#include <OneWire.h>
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 11
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
float Tfloat,T_old;
LiquidCrystal_I2C lcd(0x27,16,2);
void setup(void)
{
    sensors.begin();
    lcd.begin();
} 
void loop(void)
{
    sensors.requestTemperatures(); 
    Tfloat = sensors.getTempCByIndex(0);
    if(T_old!=Tfloat)
  {
  if  (Tfloat < 25)
  {
      lcd.setCursor(0,0);
      lcd.print("T = ");
      lcd.print(Tfloat,4);
      lcd.setCursor(0,1);
      lcd.print("        ");
      lcd.setCursor(0,1);
      lcd.print("Cool");
      delay(500);
  }
  if ((Tfloat >=25) && (Tfloat <= 34))
  {
      lcd.setCursor(0,0);
      lcd.print("T = ");
      lcd.print(Tfloat,4);
      lcd.setCursor(0,1);
      lcd.print("        ");
      lcd.setCursor(0,1);
      lcd.print("Hot");
      delay(500);
  }
  if (Tfloat > 34)
  {
      lcd.setCursor(0,0);
      lcd.print("T = ");
      lcd.print(Tfloat,4);
      lcd.setCursor(0,1);
      lcd.print("        ");
      lcd.setCursor(0,1);
      lcd.print("Very Hot");
      delay(500);
  }
  }
  T_old = Tfloat;
}