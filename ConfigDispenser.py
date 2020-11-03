import numpy as np
import os
import keyboard

while True:
    
    Info = open("Dispenser.txt", "w")
    Info.close()
    Info = open("Dispenser.txt", "r+")
    EPI = input("Deseja editar as posições dos EPIs no dispenser? s/n: ")
    if EPI == "s":
        x = 0
        while (True):
            if x < 5:
                x +=1
                EPIs = input('Posição ' + str(x) + ": ")
                Info.write(EPIs + ";" "\n")
            else:
                break
            
    elif EPI == "n":
        break
