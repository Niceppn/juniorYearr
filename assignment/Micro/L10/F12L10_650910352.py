import serial
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

ser = serial.Serial('COM3', 9600)

def forward():
    ser.write(b'F')

def backward():
    ser.write(b'B')

def stop():
    ser.write(b'S')

root = ttk.Window(themename="superhero")
root.title("Motor Control")

forward_button = ttk.Button(root, text="หมุนตามเข็มนาฬิกา", command=forward, bootstyle=SUCCESS)
forward_button.pack(pady=10)

backward_button = ttk.Button(root, text="หมุนทวนเข็มนาฬิกา", command=backward, bootstyle=DANGER)
backward_button.pack(pady=10)

stop_button = ttk.Button(root, text="หยุดหมุน", command=stop, bootstyle=WARNING)
stop_button.pack(pady=10)

root.mainloop()

ser.close()
