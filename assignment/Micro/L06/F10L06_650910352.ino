#include "Wire.h"
#include <LiquidCrystal_I2C.h> 
#define DS1307_I2C_ADDRESS 0x68 
byte second, minute, hour, dayOfWeek, date, month, year;
String x,y;
LiquidCrystal_I2C lcd(0x27,16,2);
byte decToBcd(byte val)
{
    return ( (val/10*16) + (val%10) );
}
byte bcdToDec(byte val)
{
    return ( (val/16*10) + (val%16) );
}
void setTimeDateDs1307(byte hh,byte mm,byte ss,byte dw,byte da,byte mo,byte ye)
{
    Wire.beginTransmission(DS1307_I2C_ADDRESS);
    Wire.write(0x00);
    Wire.write(decToBcd(ss)); 
    Wire.write(decToBcd(mm));
    Wire.write(decToBcd(hh));
    Wire.write(decToBcd(dw));
    Wire.write(decToBcd(da));
    Wire.write(decToBcd(mo));
    Wire.write(decToBcd(ye));
    Wire.endTransmission();
}
void getTimeDateDs1307()
{
    Wire.beginTransmission(DS1307_I2C_ADDRESS);
    Wire.write(0x00);
    Wire.endTransmission();  
    Wire.requestFrom(DS1307_I2C_ADDRESS, 7);
    second = bcdToDec(Wire.read() & 0x7f);
    minute = bcdToDec(Wire.read());
    hour = bcdToDec(Wire.read() & 0x3f);
    dayOfWeek = bcdToDec(Wire.read());
    date = bcdToDec(Wire.read());
    month = bcdToDec(Wire.read());
    year = bcdToDec(Wire.read());
    if(dayOfWeek==1)
    {
      x="Sun";
    }
    if(dayOfWeek==2)
    {
      x="Mon";
    }
    if(dayOfWeek==3)
    {
      x="Tue";
    }
    if(dayOfWeek==4)
    {
      x="Wed";
    }
    if(dayOfWeek==5)
    {
      x="Thu";
    }
    if(dayOfWeek==6)
    {
      x="Fri";
    }
    if(dayOfWeek==7)
    {
      x="Sat";
    }
    if (month==1)
    {
      y="Jan";
    }
    if (month==2)
    {
      y="Feb";
    }
    if (month==3)
    {
      y="Mar";
    }
    if (month==4)
    {
      y="Apr";
    }
    if (month==5)
    {
      y="May";
    }
    if (month==6)
    {
      y="Jun";
    }
    if (month==7)
    {
      y="Jul";
    }
    if (month==8)
    {
      y="Aug";
    }
    if (month==9)
    {
      y="Sep";
    }
    if (month==10)
    {
      y="Oct";
    }
    if (month==11)
    {
      y="Nov";
    }
    if (month==12)
    {
      y="Dec";
    }
}
void showDT(int val)
{  
    if (val<10)
    {
          lcd.print("0");
          lcd.print(val);
    }
    else
          lcd.print(val);
}
void setup() 
{
    Wire.begin();
    setTimeDateDs1307(11,25,46,4,23,5,21);
    lcd.begin();
    lcd.clear();
}
void loop()
{
    getTimeDateDs1307();
    lcd.setCursor(0,0);
    showDT(hour);
    lcd.print(":");
    showDT(minute);
    lcd.print(":");
    showDT(second);  
    lcd.setCursor(12,0);
    lcd.print(x);
    lcd.setCursor(0,1);
    showDT(date);
    lcd.print("  ");
    lcd.print(y);
    lcd.print("  20");
    showDT(year); 
    delay(1000);
}