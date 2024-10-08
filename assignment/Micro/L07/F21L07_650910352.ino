#include<LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
#define Buzzerpin 11
int Water,tempWater=0;
void setup() {
  pinMode(Buzzerpin,OUTPUT);
  lcd.begin();
  lcd.home();
  lcd.print("Level = ");
  digitalWrite(Buzzerpin,HIGH);
}
void loop() {
  Water=analogRead(A0);
  Water=map(Water,0,1023,0,100);
  if(Water!=tempWater){
    lcd.setCursor(8,0);
    lcd.print("   ");
  }
  lcd.setCursor(8,0);
  lcd.print(Water);
  lcd.print("%");
  tempWater=Water;
  if(Water>=80){
    tone(Buzzerpin,1000,300);
    delay(300);
    digitalWrite(Buzzerpin,HIGH);
  } 
}