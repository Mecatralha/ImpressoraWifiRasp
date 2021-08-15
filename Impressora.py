import serial
import serial.tools.list_ports
from time import sleep

#Deteccao da porta serial referente a impressora
com = ""
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if("USB Serial" in p[1]):
        com  = p[0]

#Configuracao da conexao serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = com
ser.open()

#Inicializacao da comunicacao
ser.write(b'\r\n\r\n')
sleep(2)
#Limpeza do buffer
ser.flushInput()

#Entrada do arquivo a ser impresso
arquivo = input("Digite o nome do arquivo: ")

#Abertura do arquivo para impressao
arq = open(arquivo)
comandos = arq.readlines()
arq.close()

#flags e variaveis para controle da impressao
leitura = 'ok'
fim = False
nLines = len(comandos)
countComandos = 0

#loop de impressao
while(not fim):
    #Condicao de descarte de linhas desnecessarias para a maquina
    if((comandos[countComandos][0] == ';') or (len(comandos[countComandos])<3)):
        countComandos += 1

    else:
        #Condicao de onde acontece o envio do G-code
        if('ok' in leitura):
            ser.write(bytes(comandos[countComandos], 'utf-8'))
            print(comandos[countComandos])
            countComandos += 1
            leitura = ''

        #Exibicao da resposta da maquina
        leitura = str(ser.readline())
        print(leitura)

    #Eventro de finalizacao do processo
    if(countComandos == nLines):
        fim = True

#Fechamento da conexao
ser.close()
