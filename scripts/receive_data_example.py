import serial
from time import sleep
ser1 = serial.Serial('COM27', 9600)
sleep(3)

while(1):
    arduinoData = ser1.read_until()
    print(arduinoData)
