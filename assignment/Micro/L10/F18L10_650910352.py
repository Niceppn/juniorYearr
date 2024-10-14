import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import serial

def show_alert(message):
    if "Vibration Detected" in message:
        alert_label.config(text="ตรวจพบการสั่นไหว!", bootstyle="danger")
    else:
        alert_label.config(text="ไม่มีการสั่นไหว", bootstyle="info")

def read_serial():
    if ser.in_waiting > 0:
        message = ser.readline().decode('utf-8').strip()
        show_alert(message)
    app.after(1000, read_serial)

ser = serial.Serial('COM3', 9600)

app = ttk.Window(themename="darkly")
app.title("การแจ้งเตือนจาก Vibration Sensor")
app.geometry("400x200")

alert_label = ttk.Label(app, text="ไม่มีการสั่นไหว", bootstyle="info", font=("Helvetica", 16))
alert_label.pack(pady=20)

app.after(1000, read_serial)
app.mainloop()