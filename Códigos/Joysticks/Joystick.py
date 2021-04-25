from Adafruit_ADS1x15 import ADS1x15 #Importando bibliotecas
from time import sleep
import time, signal, sys, os
import RPi.GPIO as GPIO


delayTime = 0.1 # 10ms de atraso no loop

ADS1015 = 0x01  # setando o conversor ADS1015

gain = 4096  # ganho aplicado ao valor de tensão obtido do joystick

sps = 64   # 64 amostras por segundo

A0 = 0    # Adicionando nomes aos canais analógicos a serem lidos
A1 = 1    # A0 = X joystick 1 (x1)
A2 = 2    # A1 = y1     ;   A2 = x2     ;   A3 = y2 
A3 = 3    

adc = ADS1x15(ic=ADS1015)

SW1 = 5 #setando pinos onde estarão conectados os botões dos joysticks
SW2 = 6

if __name__ == '__main__':  #função

    GPIO.setmode(GPIO.BCM)  #setando modo de numeração dos pinos
    GPIO.setwarnings(False)
    GPIO.setup(SW1, GPIO.IN, pull_up_down = GPIO.PUD_UP)    #setando resistores de pull-up para os botões
    GPIO.setup(SW2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    pressionadosw1 = False
    
    while True:                
        # Current values will be recorded 
        x1 = adc.readADCSingleEnded(A0, gain, sps) #realiza a leitura dos dados de cada porta do conversor AD
        y1 = adc.readADCSingleEnded(A1, gain, sps) #valores inteiros medidos de -2048 à 2047 (-4.096V à 4.096V)
        x2 = adc.readADCSingleEnded(A2, gain, sps) #porém para o joystick apenas são obtidos valores positivos, indo de 0 à 2047 
        y2 = adc.readADCSingleEnded(A3, gain, sps) #enquanto no centro, é esperado um valor de 1023. Para baixo, é esperado 0.
                                                   #Para cime é esperado 2047
        
        if not GPIO.input(SW1): #Verifucação se o botão for pressionado (usado para ativar funções específicas, ex: voltar pra de onde saiu)
            if not pressionadosw1: #Se anteriormente o botão não estava pressionado
                print("Button pressed!")
                pressionadosw1 = True
        # Caso contrário (botão não pressionado)
        else:
            pressionadosw1 = False
            
        time.sleep(delayTime)



