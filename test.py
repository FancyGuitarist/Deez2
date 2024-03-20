import serial
import tkinter as tk

# Function to update the label with received data
def update_label():
    # Read a line of data from the serial port
    data = ser.readline().decode().strip()
    
    # Print the received data
    print("Received:", data)

    # Update the label text with the received data
    label.config(text="Received: " + data)
    
    # Schedule the next update after 100 milliseconds
    root.after(100, update_label)

# Configure the serial port
ser = serial.Serial('/dev/cu.usbmodem11301', 9600) # Change 'COM3' to match your Arduino's serial port

# Create the Tkinter window
root = tk.Tk()
root.title("Arduino Data Viewer")

# Create a label to display received data
label = tk.Label(root, text="Waiting for data...")
label.pack(padx=20, pady=20)

# Start updating the label
update_label()

# Main loop to run the Tkinter application
root.mainloop()
