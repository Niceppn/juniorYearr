int ledRed = 11;
int ledGreen = 10;
int ledBlue = 9;
char key,r,g,b,c,m,y;
void setup()
{
    Serial.begin(9600);
    pinMode(ledRed,OUTPUT);
    pinMode(ledGreen,OUTPUT);
    pinMode(ledBlue,OUTPUT);
}
void loop()
{
    if(Serial.available())
    {
        key = Serial.read();
    }
    if (key == 'r')
    {
        analogWrite(ledRed,255);
        analogWrite(ledGreen,0);
        analogWrite(ledBlue,0);
    }
    if (key == 'g')
    {
        analogWrite(ledRed,0);
        analogWrite(ledGreen,255);
        analogWrite(ledBlue,0);
    }
    if (key == 'b')
    {
        analogWrite(ledRed,0);
        analogWrite(ledGreen,0);
        analogWrite(ledBlue,255);
    }
    if (key == 'c')
    {
        analogWrite(ledRed,0);
        analogWrite(ledGreen,255);
        analogWrite(ledBlue,255);
    }
    if (key == 'm')
    {
        analogWrite(ledRed,255);
        analogWrite(ledGreen,0);
        analogWrite(ledBlue,255);
    }
    if (key == 'y')
    {
        analogWrite(ledRed,255);
        analogWrite(ledGreen,255);
        analogWrite(ledBlue,0);
    }
}