import serial
import time
import pyttsx3

ser = serial.Serial('COM3', 9600)  
engine = pyttsx3.init()

def alert():
    engine.say("เกิดเหตุไฟไหม้ค่ะ ขอให้ทุกคนรีบออกจากสถานที่นี้โดยด่วนค่ะ")
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        if ser.readline().strip() == b'1':
            alert()
        time.sleep(1)
