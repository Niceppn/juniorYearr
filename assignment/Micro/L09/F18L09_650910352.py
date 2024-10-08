import serial
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

def button_press(button_number):
    arduino.write(bytes(str(button_number), 'utf-8'))

button_press(1)
time.sleep(1)
button_press(2)
time.sleep(1)

arduino.close()
