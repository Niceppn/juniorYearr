import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

while True:
    time.sleep(1)
    if arduino.in_waiting > 0:
        water_level = arduino.readline().decode('utf-8').strip()
        print(f"Water Level: {water_level}%")
