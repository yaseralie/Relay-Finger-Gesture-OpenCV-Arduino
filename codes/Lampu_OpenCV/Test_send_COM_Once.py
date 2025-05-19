# Importing Libraries
import serial
import time
ser = serial.Serial(port='COM3', baudrate=9600, timeout=1)
ser.write("on".encode())
time.sleep(1)
ser.write("off".encode())
time.sleep(1)
ser.write("on".encode())
time.sleep(1)
ser.write("off".encode())
time.sleep(1)
ser.write("on".encode())
time.sleep(1)
ser.write("off".encode())
time.sleep(1)
ser.write("on".encode())
time.sleep(1)
ser.write("off".encode())
ser.close
