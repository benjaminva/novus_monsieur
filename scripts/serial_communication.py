import serial
ser1 = serial.Serial('COM27', 9600)
ser1.write('s'.encode())
