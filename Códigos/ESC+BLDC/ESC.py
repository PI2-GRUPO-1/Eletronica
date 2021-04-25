import os     #importando biblioteca OS que permite comunicação com o sistema operacional
import time   #importando biblioteca que tem funções relacionadas a tempo necessárias ao projeto
os.system ("sudo pigpiod") #Ativando biblioteca para uso dos pinos GPIO, mais algumas funções úteis ao controle dos motores
time.sleep(1) # Delay inicial, evitando erros no início do programa
import pigpio #importando biblioteca dos pinos GPIO

BM1=8  # Setando pinos onde estão conectados os controladores ESC (ver esquemático)
BM2=23  #
BM3=24  #
BM4=25  # 

pi = pigpio.pi(); # nomeando função
pi.set_servo_pulsewidth(BM1, 0) #Controlando os pulsos pwm enviados a cada motor, no caso, todos em 0, ou seja, parados
pi.set_servo_pulsewidth(BM2, 0)
pi.set_servo_pulsewidth(BM3, 0)
pi.set_servo_pulsewidth(BM4, 0) 

valor_maximo = 1860 #Setando largura de pulso máximo em microsegundos (obtido do datasheet)
valor_minimo = 1060 #Setando largura de pulso mínimo, em micro segundos (obtido do datasheet)


def controle_manual(ESC, Speed): #Função para programar manualmente controlador ESC
    pi.set_servo_pulsewidth(ESC,Speed)
                
def calibrar(ESC):   #Função a partir da qual é possível calibrar automaticamente o controlador (usada apenas na primeira vez que o motor é conectado)
    pi.set_servo_pulsewidth(ESC, 0) #primeiramente, para-se o motor
    print("Deve-se então desconectar a bateria, para evitar acidentes")
    inp = raw_input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value) #ativa-se a máxima velocidade
        print("Conecte a bateria, quando ouvir sons de beep gradualmente abaixando sua tonalidade, aperte enter")
        inp = raw_input()
        if inp == '':            
            pi.set_servo_pulsewidth(ESC, min_value)
            print "Velocidade mínima, aguarde"
            time.sleep(12)
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            print "Armando ESC:"
             pi.set_servo_pulsewidth(ESC, max_value)
            time.sleep(1)
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
            print "Motor calibrado, pode usar outras funções caso desejado"
            controle(ESC)
            
def controle(ESC): #Função a ser usada após o motor estar calibrado, para testar diversas velocidades
    time.sleep(1)
    speed = 1460    # O valor de velociddade deve estar entre 1060 e 1860
    while True:
        pi.set_servo_pulsewidth(ESC, speed)
        if inp == "q":
            speed -= 100    # diminuindo bastante a velocidade
            print "speed = %d" % speed
        elif inp == "e":    
            speed += 100    # aumentando bastante a velocidade
            print "speed = %d" % speed
        elif inp == "d":
            speed += 10     # aumentando a velocidade um pouco 
            print "speed = %d" % speed
        elif inp == "a":
            speed -= 10     # diminuindo um pouco a velocidade
            print "speed = %d" % speed
        elif inp == "stop":
            stop()          #parando motor
            break
        elif inp == "manual":
            manual_drive()
            break
		elif inp == "arm":
			arm()
			break	
            
def arm(ESC): #Processo para armar o controlador ESC 
    print "conecte a bateria e aperte Enter"
    inp = raw_input()    
    if inp == '':
        pi.set_servo_pulsewidth(ESC, 0)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, max_value)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, min_value)
        time.sleep(1)
        control() 
        
def parada(ESC): #Código de parada do motor
    pi.set_servo_pulsewidth(ESC, 0)
    pi.stop()



if __name__ == '__main__':  #função

    #controles básicos:
    # em Z:
    #Para cima = aumentar a velocidade dos 4 motores
    #Para baixo = diminuir a velocidade dos 4 motores
    
    #Rotacionar:
    #Aumentar velocidade dos motores em uma diagonal (os que giram no mesmo sentido horário)
    #Diminuir a velocidade dos motores na outra diagonal (os que giram no mesmo sentido horário)
    
    # Em X e Y:
    #Aumentar velocidade dos dois motores na posição oposta a direção (X ou Y) para a qual deseja-se movimentar. gerando uma inclinação do drone.
    #E diminuir a velocidade dos dois motores opostos a estes, fazendo com que o drone não possua movimentação vertical, apenas horizontal
    
    # Utilização das funções para controle dos motores:
    #controle_manual(BMi, velocidade)# Use essa função para selecionar a velocidade do motor (valor entre 1060 - mínima velocidade, e 1860 - máxima velocidade)
    #calibrar(BMi)# Use essa função na primeira vez que ligar os motores para calibrá-los
    #arm(BMi)  # Use essa função pra "armar" o controlador ESC
    #controle(BMi) #use essa função pra controlar a velocidade
    #parada(BMi)    # Use essa função pra parar determinado motor