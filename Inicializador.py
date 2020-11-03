import os
import keyboard
from Identificador_nomes import iD
from Identificador_nomes import STATUS
from Identificador_nomes import CODE
from Identificador_nomes import N
import requests
while True:
        print('\nDigite o comando: ')
        comando = input('') 
        if comando == 'cadastrar':
            exec(open(r'C:\Users\Pedro\Desktop\Vision\Cadastro_faces.py', encoding="utf-8").read(),globals())
            print('\n')
            print('=====================================')
            print('== Cadastro concluido com sucesso ===')
            print('=====================================')
            print('\n')
            exec(open(r'C:\Users\Pedro\Desktop\Vision\Leitura_fotos.py', encoding="utf-8").read(),globals())
            print('\n')
            print('=====================================')
            print('= Treinamento concluido com sucesso =')
            print('=====================================')
            print('\n')
        elif comando == 'personalizar':
            print('\n')
            print('=====================================')
            print('==== Personalizacao em andamento ====')
            print('=====================================')
            print('\n')
            exec(open(r'C:\Users\Pedro\Desktop\Vision\Personalizacao.py', encoding="utf-8").read(),globals())
            print('\n')
            print('=====================================')
            print('=== Config Dispenser em andamento ===')
            print('=====================================')
            print('\n')
            exec(open(r'C:\Users\Pedro\Desktop\Vision\ConfigDispenser.py', encoding="utf-8").read(),globals())
        elif comando == 'reconhecer':
            print('\n')
            print('=====================================')
            print('==== Reconhecimento em andamento ====')
            print('=====================================')
            print('\n')
            exec(open(r'C:\Users\Pedro\Desktop\Vision\Reconhecimento_faces_arduino_dispenser_cores.py', encoding="utf-8").read(),globals())
        elif comando =='sair':
            for i in range(len(iD)):
                url1 = "https://server-vision.herokuapp.com/status"
                headers1 = {"Authorization": N}
                pload = {"id": CODE[i] , "status":"Não verificado"}
                x1 = requests.post(url = url1, headers = headers1, json = pload)
            break
        else:
            print('\n=====================================')
            print("========== Comando inválido =========")
            print('=====================================\n')

