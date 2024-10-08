#define Rpin 11
#define Gpin 10
#define Bpin 9
#define Gaspin 8
byte Colorcode[2][3]={{0,1,0},{1,0,0}};
int Status;
void setup() {
  pinMode(Gaspin,INPUT);
  for(int i=Bpin;i<=Rpin;i++)
    pinMode(i,OUTPUT);
}
void loop() {
  Status=digitalRead(Gaspin);
  digitalWrite(Rpin,Colorcode[Status][0]);
  digitalWrite(Gpin,Colorcode[Status][1]);
  digitalWrite(Bpin,Colorcode[Status][2]);
}