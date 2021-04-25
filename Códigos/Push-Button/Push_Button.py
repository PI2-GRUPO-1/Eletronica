#Importando bibliotecas necessárias
import time
import RPi.GPIO as GPIO
#Definindo pinos de IO, aos quais estão conectados os botões
B1 = 18
B2 = 23
B3 = 24
B4 = 25

#Iniciando função main
if __name__ == '__main__':
    #Ativando resistor de pullup interno da raspberry pi nos pinos
    GPIO.setmode(GPIO.BCM)  #Definindo estilo de numeração dos pinos (BCM é o apresentado no esquemático desenvolvido)
    GPIO.setup(B1, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Ativando resistor de pullup em cada um dos pinos onde estão conectados os botões
    GPIO.setup(B2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(B3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(B4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    pressionado1 = False #Considerando que inicialmente o botão não está pressionado
    pressionado2 = False
    pressionado3 = False
    pressionado4 = False
    while True:
        #Por estar sendo utilizado um resistor de pullup com o botão coenctado ao gnd, este muda para o nível lógico...
        # ... False quando pressionado
        if not GPIO.input(B1):
            if not pressionado1: #Se anteriormente o botão não estava pressionado
                print("Button pressed!")
                pressionado1 = True
        # Caso contrário (botão não pressionado)
        else:
            pressionado1 = False
        if not GPIO.input(B2):
            if not pressionado2: #Se anteriormente o botão não estava pressionado
                print("Button pressed!")
                pressionado2 = True
        # Caso contrário (botão não pressionado)
        else:
            pressionado2 = False
        if not GPIO.input(B3):
            if not pressionado3: #Se anteriormente o botão não estava pressionado
                print("Button pressed!")
                pressionado3 = True
        # Caso contrário (botão não pressionado)
        else:
            pressionado3 = False
        if not GPIO.input(B4):
            if not pressionado4: #Se anteriormente o botão não estava pressionado
                print("Button pressed!")
                pressionado4 = True
        # Caso contrário (botão não pressionado)
        else:
            pressionado4 = False
        time.sleep(0.1)