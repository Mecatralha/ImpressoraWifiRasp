import serial
import serial.tools.list_ports
from time import sleep

com = ""

ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p[0],p[1])
    if("USB Serial" in p[1]):
        com  = p[0]

#com = "/dev/ttyUSB0" 

print(com)

ser = serial.Serial()
ser.baudrate = 115200
ser.port = com
ser.open()

ser.write(b'\r\n\r\n')
sleep(2)
ser.flushInput()

ser.write(bytes('G0 X0\n', 'utf-8'))

leitura = ser.readline()
print(leitura)

ser.close()
