import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import serial
import threading

ser = serial.Serial('COM3', 9600, timeout=1)

def read_distance():
    while True:
        if ser.in_waiting > 0:
            distance = ser.readline().decode('utf-8').strip()
            distance_label.config(text=f"ระยะทาง: {distance} cm")
            distance_bar['value'] = float(distance)

root = ttk.Window(themename="superhero")
root.title("Ultrasonic Sensor Distance")

distance_label = ttk.Label(root, text="ระยะทาง: -- cm", font=("Helvetica", 24), bootstyle=PRIMARY)
distance_label.pack(pady=20)

distance_bar = ttk.Progressbar(root, bootstyle=INFO, length=400, maximum=400)
distance_bar.pack(pady=10)

sensor_image = ttk.Label(root, text="🔊", font=("Helvetica", 40))
sensor_image.pack(pady=20)

thread = threading.Thread(target=read_distance)
thread.daemon = True
thread.start()

root.mainloop()

ser.close()
