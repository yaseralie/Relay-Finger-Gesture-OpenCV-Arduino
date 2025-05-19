import serial 
import time 
import struct

ser = serial.Serial(
    port='COM3',
    baudrate =9600,           
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

k=struct.pack('B', 0xff)

string = 1
command = 't0.txt="' + str(string) + '"' 
ser.write(command.encode())
ser.write(k)
ser.write(k)
ser.write(k)
