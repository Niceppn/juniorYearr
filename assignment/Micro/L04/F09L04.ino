#include <LiquidCrystal.h>
#include <Keypad.h>

const int lcdColumns = 16; // จำนวนคอลัมน์ของ LCD
const int lcdRows = 2; // จำนวนแถวของ LCD

LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // กำหนดขาที่เชื่อมต่อกับ LCD

const byte ROWS = 4; // กำหนดจำนวนแถวของ Keypad
const byte COLS = 3; // กำหนดจำนวนคอลัมน์ของ Keypad

char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};

byte rowPins[ROWS] = {9, 8, 7, 6}; // ขาที่เชื่อมต่อกับแถวของ Keypad
byte colPins[COLS] = {A3, A2, A1}; // ขาที่เชื่อมต่อกับคอลัมน์ของ Keypad

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

int position = 0; // ตำแหน่งเริ่มต้นของตัวอักษร "B"

void setup() {
  lcd.begin(lcdColumns, lcdRows);
  lcd.setCursor(position, 0);
  lcd.print("B"); // แสดงตัวอักษร "B" ที่ตำแหน่งเริ่มต้น
}

void loop() {
  char key = keypad.getKey(); // อ่านค่าจาก Keypad

  if (key == '#') {
    if (position < lcdColumns - 1) { // ตรวจสอบว่าตำแหน่งอยู่ในขอบเขตของจอ LCD
      lcd.clear();
      position++;
      lcd.setCursor(position, 0);
      lcd.print("B");
    }
  }

  if (key == '*') {
    if (position > 0) { // ตรวจสอบว่าตำแหน่งอยู่ในขอบเขตของจอ LCD
      lcd.clear();
      position--;
      lcd.setCursor(position, 0);
      lcd.print("B");
    }
  }
}