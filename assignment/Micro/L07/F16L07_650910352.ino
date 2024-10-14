#include<LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x20,16,2); 
#define PIRpin 8
int Status;
void setup() {
  lcd.begin();
  lcd.setCursor(0,0);
}
void loop() {
  Status=digitalRead(PIRpin);
  if(Status==1){
    lcd.print("Welcome");
    delay(5000);
    lcd.clear();
    lcd.home();
  }
}