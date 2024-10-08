int x;
int sensorpin = 7;
int buzzerpin = 11;
void setup()
{
    pinMode(sensorpin,INPUT);
    pinMode(buzzerpin,OUTPUT);
    digitalWrite(buzzerpin,HIGH);
}
void loop()
{
    x = digitalRead(sensorpin);
    if (x==0)
    {
        tone(buzzerpin,800,400);
        delay(400);
        digitalWrite(buzzerpin,HIGH);
        delay(100);     
    }
}