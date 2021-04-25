from Adafruit_ADS1x15 import ADS1x15
from time import sleep
import time, signal, sys, os
import RPi.GPIO as GPIO

delayTime = 0.1 # 10ms de atraso no loop


ADS1015 = 0x01  # 12-bit ADC

gain = 1  # ganho aplicado ao valor de tensão obtido do joystick

sps = 1   # 1 amostras por segundo

A0 = 0    # Canal 0 do conversor AD

adc = ADS1x15(ic=ADS1015)


if __name__ == '__main__':

    while True:                
        # Current values will be recorded 
        Bat_Lvl = adc.readADCSingleEnded(A0, gain, sps) #realiza a leitura dos dados de cada porta do conversor AD
            
        time.sleep(delayTime)