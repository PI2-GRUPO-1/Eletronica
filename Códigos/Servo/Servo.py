import os     #importando biblioteca OS que permite comunicação com o sistema operacional
import time   #importando biblioteca que tem funções relacionadas a tempo necessárias ao projeto
os.system ("sudo pigpiod") #Ativando biblioteca para uso dos pinos GPIO, mais algumas funções úteis ao controle dos motores
time.sleep(1) # Delay inicial, evitando erros no início do programa
import pigpio #importando biblioteca dos pinos GPIO

SM=5  # Setando pino onde vai estar conectado o servo

pi = pigpio.pi(); # nomeando função
pi.set_servo_pulsewidth(SM, 0) #Controlando os pulsos pwm enviados a cada motor, no caso, todos em 0, ou seja, parados

valor_maximo = 2000 #Setando largura de pulso máximo em microsegundos (obtido do datasheet)
valor_minimo = 1000  #Setando largura de pulso mínimo, em micro segundos (obtido do datasheet)

def servo_control(angulo): #Função para programar manualmente controlador ESC
    pulse_width = 1500 + (angulo*500/90) #velocidade em 1500 resulta no motor ficando no meio, a equação do valor_maximo
                                          #leva em conta que em speed = 2000 (1500 + 500), o motor fica rotacionado em 90 graus
    pi.set_servo_pulsewidth(SM,pulse_width)
                
if __name__ == '__main__':  #função
    dir = 1 #definindo variáveis sobre o controle de movimentação do servo
    angulo = 0
        
    while True
        if dir == 1:
            angulo = angulo + 0.5 #vai movimentando o servo motor (e consequentemente o sensor Lidar)
            if angulo == 15:
                dir  = 0 #muda direção de movimentação do motor
        elif dir = 0:
            angulo  = angulo - 0.5
            if angulo == -15:
                dir  = 1
        
        servo_control(angulo) #chama a função que controla o servo motor
        time.sleep(0.1)