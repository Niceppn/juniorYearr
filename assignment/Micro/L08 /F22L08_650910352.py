import serial
import time
import requests

LINE_TOKEN = 'm0Bfu7bCPCuqEH7Na6nMvoXdOxxpXz0HVe44irt7Dai'

def send_line_notify(message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + LINE_TOKEN}
    data = {'message': message}
    requests.post(url, headers=headers, data=data)

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

while True:
    time.sleep(1)
    if arduino.in_waiting > 0:
        motion_state = arduino.readline().decode('utf-8').strip()
        
        if motion_state == "motion_detected":
            print("Motion detected!")
            send_line_notify("!!!!! พบผู้บุกรุก !!!!!")
        else:
            print("No motion detected")
