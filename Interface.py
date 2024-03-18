import serial
dev = serial.Serial("/dev/cu.usbmodem21301", 9600)

dev.write(b'1')
dev.write(b'0')
data = '1'

data.encode('utf=16')