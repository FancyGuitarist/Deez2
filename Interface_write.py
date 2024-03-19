import tkinter as tk
import serial

arduino_port = '/dev/cu.usbmodem21301'  # Change this to the appropriate port
baud_rate = 9600  # Make sure it matches the baud rate in your Arduino sketch

def send_command(command):
    ser.write(command.encode())

root = tk.Tk()
root.title("Arduino Control")

# Define functions for controlling Arduino
def turn_on_led():
    send_command('1')

def turn_off_led():
    send_command('0')
    
def blink():
    send_command('2')

# Create buttons
btn_on = tk.Button(root, text="Turn On LED", command=turn_on_led)
btn_on.pack()

btn_off = tk.Button(root, text="Turn Off LED", command=turn_off_led)
btn_off.pack()

btn_blk = tk.Button(root, text="Blink LED", command=blink)
btn_blk.pack()

# Connect to Arduino
try:
    ser = serial.Serial(arduino_port, baud_rate)
except serial.SerialException:
    print("Failed to connect to Arduino.")

root.mainloop()
