import serial
from time import sleep
ser1 = serial.Serial('COM27', 9600)
sleep(3)

for i in range(3):
    print("s")
    ser1.write("s".encode())
    sleep(3)

    print("a")
    ser1.write("a".encode())
    sleep(3)

ser1.close()
