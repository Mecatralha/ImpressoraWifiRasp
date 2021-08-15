import serial
import serial.tools.list_ports
from time import sleep

com = ""

ports = list(serial.tools.list_ports.comports())
for p in ports:
    #print(p[0],p[1])
    if("USB Serial" in p[1]):
        com  = p[0]

#com = "/dev/ttyUSB0" 

#print(com)

ser = serial.Serial()
ser.baudrate = 115200
ser.port = com
ser.open()

ser.write(b'\r\n\r\n')
sleep(2)
ser.flushInput()

lista = ['G0 X50\n', 'G0 Y50\n', 'G0 X0\n', 'G0 Y0\n']

ser.write(bytes(lista[2], 'utf-8'))

leitura = 'ok'

for i in range(5):
    for i in lista:
        #leitura = ser.readlines()
        #print(leitura)

        if ('ok' in leitura):
            ser.write(bytes(i, 'utf-8'))
            print(leitura)

        leitura = str(ser.readline())
        #print(leitura)


ser.close()
