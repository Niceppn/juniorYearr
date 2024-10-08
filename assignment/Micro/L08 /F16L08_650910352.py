import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def send_command(command):
    arduino.write(bytes(command, 'utf-8'))
    time.sleep(0.05)

while True:
    user_input = input("Enter command (a for CCW, b for CW): ")
    if user_input in ['a', 'b']:
        send_command(user_input)
    else:
        print("Invalid command")
