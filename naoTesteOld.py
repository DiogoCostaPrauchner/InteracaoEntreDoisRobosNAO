# -*- coding: utf-8 -*-

import time

from naoqi import ALProxy

RA_IP = "192.168.0.125"
RB_IP = "192.168.0.152"
PORT = 9559

mensagemsRA = ["Eu sou o Robô 1!", "Como você está hoje?", "Eu também! Ótimo dia hoje, não é mesmo?"]
mensagemsRB = ["Eu sou o Robô 2!", "Eu estou ótimo, e você?", "Sim! O sol está lindo!"]

indice1 = 0
indice2 = 0
cont1 = 0
cont2 = 0
contEnd = 0

tts_r1 = ALProxy("ALTextToSpeech", RA_IP, PORT)
tts_r2 = ALProxy("ALTextToSpeech", RB_IP, PORT)
mem_r1 = ALProxy("ALMemory", RA_IP, PORT)
mem_r2 = ALProxy("ALMemory", RB_IP, PORT)

mem_r1.insertData("Robo1Fala", "Eu sou o robô 1!")
mem_r2.insertData("Robo2Fala", "Eu sou o robô 2!")

def main():
    contEnd = 0
    while True:
        try:
            global indice1, indice2, cont1, cont2, contEnd

            msg1 = mem_r1.getData("Robo1Fala")
            if msg1 is not None:
                tts_r1.say(msg1)
                mem_r1.insertData("Robo1Fala", "")
                cont1 = (cont1 + 1) % len(mensagemsRA)
                mem_r2.raiseEvent("Robo2Fala", mensagemsRB[cont2])
                contEnd += 1

            msg2 = mem_r2.getData("Robo2Fala")
            if msg2 is not None:
                tts_r2.say(msg2)
                mem_r2.insertData("Robo2Fala", "")
                cont2 = (cont2 + 1) % len(mensagemsRB)
                mem_r1.raiseEvent("Robo1Fala", mensagemsRA[cont1])
                contEnd += 1

            if contEnd >= 5:
                print("Conversa encerrada!")
                break

        except KeyboardInterrupt:
            print("Encerrando script...")
            break

main()