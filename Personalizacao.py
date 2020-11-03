import numpy as np
import os
import keyboard

print('\n')
print('=====================================')
print('======= Personalize sua empresa =====')
print('=====================================')

while True:
    def AddCargo():
                    print('\n=====================================')
                    print('==== Personalizacao dos ocupação ====')
                    print('=====================================\n')
                    
                    repetido = 0
                    Cargos = input('Digite a ocupação: ')
                    Info = open("Personalizacao.txt", "r+")
                    linhas = Info.read()
                    if Cargos == "":
                        print("\nÉ necessário digitar a ocupação!\n")
                        AddCargo()
                    with open('Personalizacao.txt') as f:
                        if( linhas != None):
                            for l_num, l in enumerate(f, 1):
                                teste4 = l.index("-") - 1
                                if(Cargos == l[0:teste4]):
                                    print("\nOcupação repetida")
                                    resposta = input("\n-> Deseja alterar as definições? s/n: ")
                                    repetido = 1
                                    break
                                
                        def AddEPI():
                           x = 1
                           while (True):
                               EPI = input('EPI' + str(x) + ": ")
                               if(str(EPI)!=""):
                                   x+=1
                                   if(x<6):
                                       opccao1 = input("\n-> Deseja adicionar mais algum EPI para essa ocupação? s/n: ")
                                       if opccao1 == "s":
                                           if(x==2):
                                               Info.write(Cargos + " - ")
                                               Info.write(EPI)
                                           elif(x>2):
                                               Info.write(" , " + EPI)
                                       elif opccao1 == "n":
                                            if(x==2):
                                               Info.write(Cargos + " - ")
                                               Info.write(EPI + ";" + "\n")
                                               opccao2 = input("\n-> Deseja adicionar mais alguma ocupação? s/n: ")
                                            if (x>2):
                                                Info.write(" , " + EPI + ";" + "\n")
                                                opccao2 = input("\n-> Deseja adicionar mais alguma cocupação? s/n: ")
                                            if(opccao2=="s"):
                                                Info.close()
                                                AddCargo()
                                                break
                                            elif(opccao2 == "n"):
                                                Info.close()
                                                break
                                   elif x>= 6:
                                        Info.write(" , " + EPI + ";" + "\n")
                                        print("\nVocê atingiu o limite de EPIs\n")
                                        opccao2 = input("\n-> Deseja adicionar mais alguma ocupação? s/n: ")
                                        if(opccao2=="s"):
                                            Info.close()
                                            AddCargo()
                                            break
                                        elif(opccao2 == "n"):
                                            Info.close()
                                            break
                               elif(str(EPI)== ""):
                                   print("\nDigite o EPI dessa ocupação!")
                        if(repetido == 1):
                            if(resposta == "s"):
                                Info = open("Personalizacao.txt", "r+")
                                linhas2 = Info.readlines()
                                Info.close()
                                Info = open("Personalizacao.txt", "w")
                                Info.close()
                                Info = open("Personalizacao.txt", "r+")
                                for line in linhas2:
                                    teste3 = line.index("-") - 1
                                    if(line[0:teste3] != Cargos):
                                            Info.write(line)
                                AddEPI()
                            elif(resposta == "n"):
                                AddCargo()
                        if(repetido == 0):
                            AddEPI()

    def AddCor():
                    repetido = 0
                    Info = open("cores_equipamentos.txt", "r+")
                    linhas = Info.read()
                    print('\n')
                    print('=====================================')
                    print('====== Personalizacao das cores =====')
                    print('=====================================\n')
                    
                    EPI = input('\nDigite o EPI para configuração: ')
                    if EPI == "":
                        AddCor()
                    with open('cores_equipamentos.txt') as f:
                       if(linhas != None):
                          for l_num, l in enumerate(f, 1):
                              teste4 = l.index("-") - 1
                              if(EPI == l[0:teste4]):
                                 print("EPI repetido!")
                                 resposta = input("\n-> Deseja alterar as definições? s/n: ")
                                 repetido = 1
                                 break
                    def Add_COR_EPI():
                        x = 0
                        while (True):
                            linhas2 = Info.readlines()
                            COR = input("Digite a cor do EPI: ")
                            print("\n")
                            for line in linhas2:
                                teste3 = line.index("-") + 2
                                teste2 = line.index(";")
                                if(line[teste3:teste2] == COR):
                                     print("\nCor repetida!")
                                     Add_COR_EPI()
                            if(str(COR)== ""):
                                if(x==0):
                                  print("\nDigite a cor desse EPI")
                            elif(str(COR)!= ""):
                                  opccao1 = input("\n-> Deseja adicionar mais alguma cor para algum EPI? s/n: ")
                                  if(opccao1 == "s"):
                                    Info.write(EPI + " - ")
                                    Info.write(COR + ";" + "\n")
                                    Info.close()
                                    AddCor()
                                    break
                                  if(opccao1 == "n"):
                                    Info.write(EPI + " - ")
                                    Info.write(COR + ";" + "\n")
                                    Info.close()
                                    break
                    if(repetido == 1):
                        if(resposta == "s"):
                            Info = open("cores_equipamentos.txt", "r+")
                            linhas2 = Info.readlines()
                            Info.close()
                            Info = open("cores_equipamentos.txt", "w")
                            Info.close()
                            Info = open("cores_equipamentos.txt", "r+")
                            for line in linhas2:
                                teste3 = line.index("-") - 1
                                if(line[0:teste3] != EPI):
                                        Info.write(line)
                            Add_COR_EPI()
                        elif(resposta == "n"):
                                AddCor()
                    if(repetido == 0):
                        Add_COR_EPI()
    def opccao():
        a = 1
        opccao = input("\nDigite 1 para personalizar a configuração das ocupações \nou 2 para personalizar a configuração das cores dos EPIs \nou 3 para sair: ")
        opccao_opccao = input("\nVocê tem certeza da sua escolha? s/n: ")
        print('\n=====================================\n')
        if opccao_opccao == "s":
            if opccao == "2":
                AddCor()
            elif opccao == "1":   
                AddCargo()
            elif opccao == "3":
                a = 0
        return a
    opccao = opccao()
    if opccao == 0:
        break
    
