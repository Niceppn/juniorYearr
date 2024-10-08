int x;
int sensorpin = 7;
int redpin = 6;
int greenpin = 5;
int bluepin = 3;

void setup()
{    
    pinMode(sensorpin,INPUT);
    pinMode(redpin,OUTPUT);
    pinMode(greenpin,OUTPUT);
    pinMode(bluepin,OUTPUT);
}
void loop()
{
    x = digitalRead(sensorpin);
    if (x==0)
    {
        analogWrite(redpin,0);
        analogWrite(greenpin,255);
        analogWrite(bluepin,0);
    }
    else
    {
        analogWrite(redpin,255);
        analogWrite(greenpin,0);
        analogWrite(bluepin,0);
    }
    }