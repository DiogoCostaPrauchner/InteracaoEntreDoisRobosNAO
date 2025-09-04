# -*- coding: utf-8 -*-

#Formato:
#Comentário
#Código

#Versão inicial feita por Diogo Costa Prauchner

import time
from naoqi import ALProxy

RA_IP = "192.168.0.125" #IP Do robô A
RB_IP = "192.168.0.152" #IP Do robô B
PORT = 9559             #Porta utilizada pelos dois robôs

#Mensagens utilizadas pelos robôs nas conversas
mensagemsRA = ["Eu sou o Robô 1!", "Como você está hoje, Robô 2?", "Eu também! Ótimo dia hoje, não é mesmo?",
               "Sejam Bem-Vindos...", "frase 11"]
mensagemsRB = ["E eu sou o Robô 2!", "Eu estou ótimo, e você, Robô 1?", "Sim! O sol está lindo!",
              "Ao Espaço Mais Inovação...", "frase 12"]

#Apenas números para testar mais rapidamente a sequencia da conversa
#mensagemsRA = ["1", "3", "5", "7", "11"]
#mensagemsRB = ["2", "4", "6", "8", "12"]

#Inicialização dos contadores utilizados para a lógica de conversa
cont1 = 0
cont2 = 0
contEnd = 0

#Proxy para módulo de fala animada
ttsA_r1 = ALProxy("ALAnimatedSpeech", RA_IP, PORT)
#ttsA_r2 = ALProxy("ALAnimatedSpeech", RB_IP, PORT)
config = {"bodyLanguageMode": "contextual"}

#Substituido por ttsA_rx, que funciona da mesma maneira que o bloco "Animated Say" do Choregraphe
#Manter no código caso seja necessário no futuro
#Robô 2 ainda utiliza tts normal pois está com problemas nas articulações/engrenagens
#tts_r1 = ALProxy("ALTextToSpeech", RA_IP, PORT)
tts_r2 = ALProxy("ALTextToSpeech", RB_IP, PORT)

#Proxy para módulo de memória
mem_r1 = ALProxy("ALMemory", RA_IP, PORT)
mem_r2 = ALProxy("ALMemory", RB_IP, PORT)

#Inicialização para garantir que o código funciona
mem_r1.insertData("Robo1Fala", "Eu sou o robô 1!")
mem_r2.insertData("Robo2Fala", "E eu sou o robô 2!")

def main():
    contEnd = 0
    while True:
        try:
            global cont1, cont2, contEnd

            msg1 = mem_r1.getData("Robo1Fala")
            if msg1 is not None:
                ttsA_r1.say(msg1, config)
                mem_r1.insertData("Robo1Fala", "")
                cont1 = (cont1 + 1) % len(mensagemsRA)
                mem_r2.raiseEvent("Robo2Fala", mensagemsRB[cont2])
                contEnd += 1
                print("Valor de contEnd: " + str(contEnd))

            msg2 = mem_r2.getData("Robo2Fala")
            if msg2 is not None:
                tts_r2.say(msg2)
                mem_r2.insertData("Robo2Fala", "")
                cont2 = (cont2 + 1) % len(mensagemsRB)
                mem_r1.raiseEvent("Robo1Fala", mensagemsRA[cont1])
                contEnd += 1
                print("Valor de contEnd: " + str(contEnd))

            #A partir dessa parte usar apenas contEnd para definir quando os robôs vão falar juntos
            #ou quando que vai terminar a conversa
            #Frases 9, 10
            if contEnd == 8:
                ttsA_r1.post.say("Da Unijuí!", config)
                #Usar time.sleep() com um valor baixo pois post.say não está funcionando corretamente
                time.sleep(0.05)
                tts_r2.post.say("Da Unijuí!")
                contEnd += 1
                print("Valor de contEnd: " + str(contEnd))

            if contEnd == 11:
                print("Conversa encerrada!")
                break

        except KeyboardInterrupt:
            print("Encerrando script...")
            break

main()