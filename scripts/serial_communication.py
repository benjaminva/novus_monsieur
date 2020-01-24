import serial
from time import sleep
ser1 = serial.Serial('COM27', 115200)
sleep(3)  # wait some time to allow the port to start

while(1):
    arduinoData = ser1.read_until()
    print(arduinoData)
