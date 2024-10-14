const int trigPin = 9;    // ขาที่เชื่อมต่อกับ Trig ของ Ultrasonic Sensor
const int echoPin = 10;   // ขาที่เชื่อมต่อกับ Echo ของ Ultrasonic Sensor
const int redPin = 5;     // ขาที่เชื่อมต่อกับขา R ของ LED RGB
const int greenPin = 6;   // ขาที่เชื่อมต่อกับขา G ของ LED RGB
const int bluePin = 7;    // ขาที่เชื่อมต่อกับขา B ของ LED RGB

void setup() {
  pinMode(trigPin, OUTPUT);  // กำหนดขา Trig เป็น Output
  pinMode(echoPin, INPUT);   // กำหนดขา Echo เป็น Input
  pinMode(redPin, OUTPUT);   // กำหนดขา R ของ LED RGB เป็น Output
  pinMode(greenPin, OUTPUT); // กำหนดขา G ของ LED RGB เป็น Output
  pinMode(bluePin, OUTPUT);  // กำหนดขา B ของ LED RGB เป็น Output
  Serial.begin(9600);        // เริ่มการสื่อสาร Serial
}

void loop() {
  long duration;
  int distance;

  // ส่งสัญญาณ Ultrasonic
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // รับสัญญาณสะท้อนกลับ
  duration = pulseIn(echoPin, HIGH);

  // คำนวณระยะทาง (เซนติเมตร)
  distance = duration * 0.034 / 2;

  // แสดงผลระยะทาง
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // ตรวจสอบระยะทางแล้วปรับสี LED
  if (distance < 35) {
    // ถ้าระยะน้อยกว่า 35 cm ให้แสดงสีแดง
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, LOW);
  } else {
    // ถ้าระยะมากกว่าหรือเท่ากับ 35 cm ให้แสดงสีเขียว
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, HIGH);
    digitalWrite(bluePin, LOW);
  }

  delay(100); // หน่วงเวลาเพื่อให้การแสดงผลมีเสถียรภาพ
}