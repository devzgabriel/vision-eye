# Programa utilizado para o reconhecimento das faces em tempo real
# As faces precisam estar nas mesmas dimensões 


import serial
import urllib.request
import numpy as np
from cv2 import cv2
import os
import re
import sys
import Identificador_nomes
from Identificador_nomes import iD
from Identificador_nomes import STATUS
from Identificador_nomes import CODE
from Identificador_nomes import N
from Identificador_nomes import Names
from Identificador_nomes import Y
import keyboard
import time
import requests
arduino = serial.Serial()
arduino.port = 'COM3'
time.sleep(1)

arduino.open()
url='IP da câmera fornecido pelo app IP Webcam'

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml') 
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml') 

recognise = cv2.face.EigenFaceRecognizer_create(15,4000)                        # Cria o identifcador EIGEN FACE
recognise.read("Recogniser/trainingDataEigan.xml")                              # Carrega as informações do "treinamento"
funcionarios = []
verificados = []
funcverificados = []
idverific = []
a = 0
def save():
    for i in range(len(CODE)):
        if STATUS[i] == "Verificado":
            funcverificados.append(Names[i])
            idverific.append(CODE[i])
save()
def processo():
    a = 1
    cap = cv2.VideoCapture(0)                                                       # Habilita a câmera
    ID = 0
    Teste = 0
    if Y == 1:
        while True:
            ret, img = cap.read()                                                       # Leitura da câmera
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Imagem da câmera e preto e branco
            faces = face_cascade.detectMultiScale(gray, 1.3,5)                         # Detecta as faces e armazena as posições
            for (x, y, w, h) in faces:                                                  # Define as dimensões da imagem                                                                    # Quanto melhor o reconhecimento dos olhos, melhor o reconhecimento da face
                gray_face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))              # A face é recortada e redimensionada
                eyes = eye_cascade.detectMultiScale(gray_face)
                for (ex, ey, ew, eh) in eyes:
                    ID, conf = recognise.predict(gray_face)                             # Determina o ID da foto
                    NAME = Identificador_nomes.ID2Name(ID, conf)
                    Cargo =Identificador_nomes.ID3Name(ID,conf)
                    def reconhecer_cargo():
                        Cargo =Identificador_nomes.ID3Name(ID,conf)
                        Info = open("Personalizacao.txt", "r+")
                        linhas = Info.readlines()

                        EPI = "cargo nao localizado"

                        cargo = Cargo

                        epis = []

                        #print(len(cargo))

                        #print(str(linhas))

                        for line in linhas:
                            if(line[0:len(cargo)] == str(cargo)):
                                indice = line.index("-") - 1
                                EPI = line[(indice+3):(len(line)-2)]

                        EPInovo = EPI
                        
                        while True:
                            if re.search('\\b , \\b', EPInovo, re.IGNORECASE):
                                indiceEPI = EPInovo.index(",")
                                epis.append(str(EPInovo[0:indiceEPI-1]))
                                EPInovo = EPInovo[indiceEPI+2:len(EPInovo)]
                                            
                            else:
                                epis.append(str(EPInovo))
                                Info.close()
                                break

                        EPI = []
                        EPI.clear()
                        COR = []
                        COR.clear()
                        for i in range(len(epis)):
                            Info = open("cores_equipamentos.txt", "r+")
                            linhas = Info.readlines()
                            EPI.append(epis[i])

                            for line in linhas:
                                if(line[0:len(epis[i])] == str(epis[i])):
                                    indice = line.index("-") - 1
                                    COR.append(line[(indice+3):(len(line)-2)])
                        return EPI, COR
                    def dispenser():
                        Info = open("Dispenser.txt", "r+")
                        linhas = Info.readlines()
                        EPI, COR = reconhecer_cargo()
                        for i in range(len(EPI)):
                            for a in range(len(linhas)):  
                                if linhas[a] == EPI[i]+ ";" + "\n":
                                    arduino.write(b':')
                                    if a+1 == 1:
                                        time.sleep(1)
                                        arduino.write(b'a')
                                        time.sleep(1)
                                    elif a+1 == 2:
                                        time.sleep(1)
                                        arduino.write(b'b')
                                        time.sleep(1)
                                    elif a+1 == 3:
                                        time.sleep(1)
                                        arduino.write(b'c')
                                        time.sleep(1)
                                    elif a+1 == 4:
                                        time.sleep(1)
                                        arduino.write(b'd')
                                        time.sleep(1)
                                    elif a+1 == 5:
                                        time.sleep(1)
                                        arduino.write(b'e')
                                        time.sleep(1)
                                    arduino.write(b'z')
                    Identificador_nomes.DispID(x, y, w, h, NAME, gray)
                    Identificador_nomes.DispID2(x, y, w, h, Cargo, gray)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        reconhecer_cargo()
                        Teste = ID
                        print("\n")
                        print('====== FUNCIONÁRIO IDENTIFICADO =====')
                        print('-> Dados do funcionário:')
                        print('-> Nome: ' + NAME)
                        print('-> Ocupação: ' + Cargo)
                        print('=====================================\n')
                        dispenser1 = input("Deseja acionar o dispenser? s/n ")
                        if dispenser1 == "s":
                            print('\n=====================================')
                            print('========= ATIVANDO DISPENSER ========')
                            print('=====================================\n')
                            dispenser()
                        else:
                            break
                      
            if Teste!=0:
                break
            cv2.imshow('Sisitema de reconhecimento de faces EIGEN FACE', gray)
    cap.release()
    cv2.destroyAllWindows()
    cap2 = cv2.VideoCapture(0)
    while True:
        #ret, img = cap2.read()                                                       # Leitura da câmera
        #gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                               # Imagem da câmera e preto e branco                       
        imgResp=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)
        cv2.imshow('Sistema de reconhecimento de equipamentos', cv2.resize(img, (640, 480)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            img_name = "{}.png".format(str(Teste)+"." + NAME)
            path = r'C:\Users\Pedro\Desktop\Checagem'
            cv2.imwrite(os.path.join(path , img_name), img)
            print('\n=====================================')
            print('==== Foto capturada com sucesso! ====')
            print('=====================================\n')
            break
    cap2.release()
    cv2.destroyAllWindows()
    while True:
        if keyboard.is_pressed('g'):
            for f_name in os.listdir(r'C:\Users\Pedro\Desktop\Checagem'):
                if (f_name.startswith(str(Teste)) and f_name.endswith('.png')):
                    imagem = r'C:\Users\Pedro\Desktop\Checagem' + '\\' + f_name
                    img = cv2.imread(imagem)
                    
                    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

                    fonte = cv2.FONT_HERSHEY_SIMPLEX
                    def vermelho():
                        cor = 0
                        lowerRed = np.array([0,100,100])
                        upperRed = np.array([10,255,255])
                        mask = cv2.inRange(imgray, lowerRed, upperRed)
                        result1 = cv2.bitwise_and(img, img, mask = mask)
                        gray1 = cv2.cvtColor(result1, cv2.COLOR_BGR2GRAY)
                        _,gray1 = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                        contours1, hierarchy = cv2.findContours(gray1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                        EPI, COR = reconhecer_cargo()
                        EPIa = "EPI não reconhecido"
                        for i in range(len(EPI)):
                            if(COR[i]) == 'vermelho':
                                EPIa = EPI[i]
                        if contours1:
                            maxArea1 = cv2.contourArea(contours1[0])
                            contourId1 = 0
                            i = 0
                            for cnt1 in contours1:
                                if maxArea1 < cv2.contourArea(cnt1):
                                    maxArea1 = cv2.contourArea(cnt1)
                                    contourId1 = i
                                i += 1
                
                            cnt1 = contours1[contourId1]
                            maxArea12 = cv2.contourArea(contours1[0])
                            contourId12 = 0
                            j = 0
                            for cnt12 in contours1:
                                if maxArea12 < cv2.contourArea(cnt12) and j != contourId1:
                                    maxArea12 = cv2.contourArea(cnt12)
                                    contourId12 = j
                                j += 1
                
                            cnt12 = contours1[contourId12]

                            maxArea13 = cv2.contourArea(contours1[0])
                            contourId13 = 0
                            k = 0
                            for cnt13 in contours1:
                                if maxArea13 < cv2.contourArea(cnt13) and k != contourId1 and k != contourId12:
                                    maxArea13 = cv2.contourArea(cnt13)
                                    contourId13 = k
                                k += 1
                            cnt13 = contours1[contourId13]
                            if(maxArea1> 30.0):
                                cv2.drawContours(img, [cnt1,cnt12,cnt13], -1, (0,0,0), 3)
                                print("-> " + EPIa+ ' colocado(a)(s)')
                            else:
                                print("-> " + EPIa + ' não colocado(a)(s)')
                                cor = 1
                        else:
                            print("-> " + EPIa + ' não colocado(a)(s)')
                            cor = 1
                        return cor
                    def amarelo():
                        cor = 0
                        lowerYellow = np.array([25, 50, 0],np.uint8)
                        upperYellow = np.array([50, 255, 255],np.uint8)
                        mask2 = cv2.inRange(imgray, lowerYellow, upperYellow)
                        result2 = cv2.bitwise_and(img, img, mask =  mask2)
                        gray2= cv2.cvtColor(result2, cv2.COLOR_BGR2GRAY)
                        _,gray2= cv2.threshold(gray2, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                        contours2, hierarchy = cv2.findContours(gray2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                        EPI, COR = reconhecer_cargo()
                        EPIa = "EPI não reconhecido"
                        for i in range(len(EPI)):
                            if(COR[i]) == 'amarelo':
                                EPIa = EPI[i]
                        if contours2:
                            maxArea2 = cv2.contourArea(contours2[0])
                            contourId2 = 0
                            i = 0
                            for cnt2 in contours2:
                                if maxArea2 < cv2.contourArea(cnt2):
                                    maxArea2 = cv2.contourArea(cnt2)
                                    contourId2 = i
                                i += 1
                
                            cnt2 = contours2[contourId2]
                            maxArea22 = cv2.contourArea(contours2[0])
                            contourId22 = 0
                            j = 0
                            for cnt22 in contours2:
                                if maxArea22 < cv2.contourArea(cnt22) and j != contourId2:
                                    maxArea22 = cv2.contourArea(cnt22)
                                    contourId22 = j
                                j += 1
                
                            cnt22 = contours2[contourId22]

                            maxArea23 = cv2.contourArea(contours2[0])
                            contourId23 = 0
                            k = 0
                            for cnt23 in contours2:
                                if maxArea23 < cv2.contourArea(cnt23) and k != contourId2 and k != contourId22:
                                    maxArea23 = cv2.contourArea(cnt23)
                                    contourId23 = k
                                k += 1
                            cnt23 = contours2[contourId23]
                            if(maxArea2> 30.0):
                                cv2.drawContours(img, [cnt2,cnt22, cnt23], -1, (0,0,0), 3)
                                print("-> " + EPIa+ ' colocado(a)(s)')
                            else:
                                print("-> " + EPIa + ' não colocado(a)(s)')
                                cor = 1
                        else:
                            print("-> " + EPIa + ' não colocado(a)(s)')
                            cor = 1
                        return cor
                    def azul():
                        cor = 0
                        lowerBlue = np.array([100,50,50],np.uint8)
                        upperBlue = np.array([125,255,255],np.uint8)
                        mask3 = cv2.inRange(imgray, lowerBlue, upperBlue)
                        result3 = cv2.bitwise_and(img, img, mask = mask3)
                        gray3 = cv2.cvtColor(result3, cv2.COLOR_BGR2GRAY)
                        _,gray3 = cv2.threshold(gray3, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                        contours3, hierarchy = cv2.findContours(gray3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                        EPI, COR = reconhecer_cargo()
                        EPIa = "EPI não reconhecido"
                        for i in range(len(EPI)):
                            if(COR[i]) == 'azul':
                                EPIa = EPI[i]
                        if contours3:
                            maxArea3 = cv2.contourArea(contours3[0])
                            contourId3 = 0
                            i = 0
                            for cnt3 in contours3:
                                if maxArea3 < cv2.contourArea(cnt3):
                                    maxArea3 = cv2.contourArea(cnt3)
                                    contourId3 = i
                                i += 1
                
                            cnt3 = contours3[contourId3]
                            maxArea32 = cv2.contourArea(contours3[0])
                            contourId32 = 0
                            j = 0
                            for cnt32 in contours3:
                                if maxArea32 < cv2.contourArea(cnt32) and j != contourId3:
                                    maxArea32 = cv2.contourArea(cnt32)
                                    contourId32 = j
                                j += 1
                
                            cnt32 = contours3[contourId32]

                            maxArea33 = cv2.contourArea(contours3[0])
                            contourId33 = 0
                            k = 0
                            for cnt33 in contours3:
                                if maxArea33 < cv2.contourArea(cnt33) and k != contourId3 and k != contourId32:
                                    maxArea33 = cv2.contourArea(cnt33)
                                    contourId33 = k
                                k += 1
                            cnt33 = contours3[contourId33]
                            if(maxArea3> 30.0):
                                cv2.drawContours(img, [cnt3,cnt32, cnt33], -1, (0,0,0), 3)
                                print("-> " + EPIa+ ' colocado(a)(s)')
                            else:
                                print("-> " + EPIa + ' não colocado(a)(s)')
                                cor = 1
                        else:
                            print("-> " + EPIa + ' não colocado(a)(s)')
                            cor = 1
                        return cor
                    def laranja():
                        cor = 0
                        lowerOrange = np.array([12, 100, 20],np.uint8)
                        upperOrange= np.array([22, 255, 255],np.uint8)
                        mask4 = cv2.inRange(imgray, lowerOrange, upperOrange)
                        result4 = cv2.bitwise_and(img, img, mask = mask4)
                        gray4 = cv2.cvtColor(result4, cv2.COLOR_BGR2GRAY)
                        _,gray4 = cv2.threshold(gray4, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                        contours4, hierarchy = cv2.findContours(gray4,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                        EPI, COR = reconhecer_cargo()
                        EPIa = "EPI não reconhecido"
                        for i in range(len(EPI)):
                            if(COR[i]) == 'laranja':
                                EPIa = EPI[i]
                        if contours4:
                            maxArea4 = cv2.contourArea(contours4[0])
                            contourId4 = 0
                            i = 0
                            for cnt4 in contours4:
                                if maxArea4 < cv2.contourArea(cnt4):
                                    maxArea4 = cv2.contourArea(cnt4)
                                    contourId4 = i
                                i += 1
                
                            cnt4 = contours4[contourId4]
                            maxArea42 = cv2.contourArea(contours4[0])
                            contourId42 = 0
                            j = 0
                            for cnt42 in contours4:
                                if maxArea42 < cv2.contourArea(cnt42) and j != contourId4:
                                    maxArea42 = cv2.contourArea(cnt42)
                                    contourId42 = j
                                j += 1
                
                            cnt42 = contours4[contourId42]

                            maxArea43 = cv2.contourArea(contours4[0])
                            contourId43 = 0
                            k = 0
                            for cnt43 in contours4:
                                if maxArea43 < cv2.contourArea(cnt43) and k != contourId4 and k != contourId42:
                                    maxArea43 = cv2.contourArea(cnt43)
                                    contourId43 = k
                                k += 1
                            cnt43 = contours4[contourId43]
                            if(maxArea4> 30.0):
                                cv2.drawContours(img, [cnt4,cnt42,cnt43], -1, (0,0,0), 3)
                                print("-> " + EPIa+ ' colocado(a)(s)')
                            else:
                                print("-> " + EPIa + ' não colocado(a)(s)')
                                cor = 1
                        else:
                            print("-> " + EPIa + ' não colocado(a)(s)')
                            cor = 1
                        return cor
                                
                    def verde():
                        cor = 0 
                        lowerGreen = np.array([36, 25, 25],np.uint8)
                        upperGreen= np.array([70, 255,255],np.uint8)
                        mask5 = cv2.inRange(imgray, lowerGreen, upperGreen)
                        result5 = cv2.bitwise_and(img, img, mask = mask5)
                        gray5 = cv2.cvtColor(result5, cv2.COLOR_BGR2GRAY)
                        _,gray5 = cv2.threshold(gray5, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                        contours5, hierarchy = cv2.findContours(gray5,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                        EPI, COR = reconhecer_cargo()
                        EPIa = "EPI não reconhecido"
                        for i in range(len(EPI)):
                            if(COR[i]) == 'verde':
                                EPIa = EPI[i]
                        if contours5:
                            maxArea5 = cv2.contourArea(contours5[0])
                            contourId5 = 0
                            i = 0
                            for cnt5 in contours5:
                                if maxArea5 < cv2.contourArea(cnt5):
                                    maxArea5 = cv2.contourArea(cnt5)
                                    contourId5 = i
                                i += 1
                
                            cnt5 = contours5[contourId5]
                            maxArea52 = cv2.contourArea(contours5[0])
                            contourId52 = 0
                            j = 0
                            for cnt52 in contours5:
                                if maxArea52 < cv2.contourArea(cnt52) and j != contourId5:
                                    maxArea52 = cv2.contourArea(cnt52)
                                    contourId52 = j
                                j += 1
                
                            cnt52 = contours5[contourId52]

                            maxArea53 = cv2.contourArea(contours5[0])
                            contourId53 = 0
                            k = 0
                            for cnt53 in contours5:
                                if maxArea53 < cv2.contourArea(cnt53) and k != contourId5 and k != contourId52:
                                    maxArea53 = cv2.contourArea(cnt53)
                                    contourId53 = k
                                k += 1
                            cnt53 = contours5[contourId53]
                            if(maxArea5> 30.0):
                                cv2.drawContours(img, [cnt5,cnt52,cnt53], -1, (0,0,0), 3)
                                print("-> " + EPIa+ ' colocado(a)(s)')
                            else:
                                print("-> " + EPIa + ' não colocado(a)(s)')
                                cor = 1
                        else:
                            print("-> " + EPIa + ' não colocado(a)(s)')
                            cor = 1
                        return cor
                    def vetor():
                        funcionarios, ids = Identificador_nomes.Nomes()
                        naoverificados = []
                        if ((NAME in funcionarios) and (ID not in idverific)):
                                funcverificados.append(NAME)
                                idverific.append(ID)
                                ID2 = ID -1
                                if str(ID) in iD:
                                    if STATUS[ID2] == "Não verificado" or STATUS[ID2] == "Em intervalo" or STATUS[ID2] == "Ausente":
                                        url1 = "https://server-vision.herokuapp.com/status"
                                        headers1 = {"Authorization": N}
                                        pload = {"id": CODE[ID2] , "status":"Verificado"}
                                        x1 = requests.post(url = url1, headers = headers1, json = pload)
                                    else:
                                        print("Funcionário já verificado!")
                        def nverificado(teste):
                            if(teste in funcverificados):
                                return False
                            else:
                                return True
                        def verificado(teste):
                            if(teste in funcverificados):
                                return True
                            else:
                                return False
                        verificados = filter(verificado,funcionarios)
                        while(True):
                            if keyboard.is_pressed('v'):
                                print("\n\n============================")
                                print("Funcionários verificados:")
                                print("============================")
                                for s in verificados:
                                    print("- " + s)
                                print("\n\n")
                                print("============================")
                                print("Funcionários não verificados:")
                                print("============================")
                                naoverificados = filter(nverificado, funcionarios)
                                if len(list(naoverificados)) != 0:
                                    naoverificados = filter(nverificado, funcionarios)
                                    for s in naoverificados:
                                        print("- " + s)
                                else:
                                    print("\n-> Todos os funcionários já foram verificados\n")
                                print("\n\n")
                                pergunta = input("Deseja verificar mais algum funcionário? s/n ")
                                if pergunta == 's':
                                    processo()
                                    break
                                else:
                                    print("\n\n")
                                    print("============================")
                                    print("Funcionários ausentes:")
                                    print("============================")
                                    naoverificados = filter(nverificado, funcionarios)
                                    for s in iD:
                                        if s not in str(idverific):
                                            url1 = "https://server-vision.herokuapp.com/status"
                                            headers1 = {"Authorization": N}
                                            pload = {"id": CODE[int(s)-1] , "status":"Ausente"}
                                            x1 = requests.post(url = url1, headers = headers1, json = pload)  
                                    for s in naoverificados:
                                        print("- " + s)
                                    print("\n\n")
                                    opccao = input ("Deseja sair para um intervalo? s/n ")
                                    if opccao  == "s":
                                        print("\n")
                                        opccao1 = input("Digite seu nome: ")
                                        opccao2 = input ("Digite seu ID: ")
                                        if opccao1 in funcverificados:
                                            opccao3 = int(opccao2)
                                            opccao4 = opccao3 -1
                                            if opccao2 in str(idverific) and STATUS[opccao4] == "Verificado":
                                                url1 = "https://server-vision.herokuapp.com/status"
                                                headers1 = {"Authorization": N}
                                                pload = {"id": CODE[(opccao4)] , "status":"Em intervalo"}
                                                x1 = requests.post(url = url1, headers = headers1, json = pload)
                                                funcverificados2 = []
                                                idverific2 = []
                                                for i in range(len(funcverificados)):
                                                    if opccao1 != funcverificados[i]:
                                                        funcverificados2.append(funcverificados[i])
                                                funcverificados.clear()        
                                                for i in funcverificados2:
                                                    funcverificados.append(i)
                                                for i in range(len(idverific)):
                                                    if opccao2 != str(idverific[i]):
                                                        idverific2.append(idverific[i])
                                                idverific.clear()        
                                                for i in idverific2:
                                                    idverific.append(i)
                                                processo()
                                            else:
                                                print("\n\n============================")
                                                print("Coloque as informações corretas!!!")
                                                print("============================")
                                                vetor()
                                        else:
                                            print("\n\n============================")
                                            print("Coloque as informações corretas!!!")
                                            print("============================")
                                            vetor()
                                    elif opccao == "n":
                                        break
                    EPI, COR = reconhecer_cargo()
                    cor1 = 0
                    cor2 = 0
                    cor3 = 0
                    cor4 = 0
                    cor5 = 0
                    for i in range(len(EPI)):
                        if COR[i] == 'azul':
                            cor1 = 0
                            cor1 = azul()
                        elif COR[i] == 'vermelho':
                            cor2 = 0
                            cor2 = vermelho()
                        elif COR[i] == 'amarelo':
                            cor3 = 0
                            cor3 = amarelo()
                        elif COR[i] == 'laranja':
                            cor4 = 0
                            cor4 = laranja() 
                        elif COR[i] == 'verde':
                            cor5 = 0
                            cor5 = verde()
                    if cor1 == 1 or cor2 == 1 or cor3 == 1 or cor4 == 1 or cor5 ==1:
                        arduino.write(b':')
                        time.sleep(1)
                        arduino.write(b'x')
                        time.sleep(1)
                        arduino.write(b'z')
                        processo()
                    cv2.imshow(f_name,cv2.resize(img, (640, 480)))
                    cv2.imwrite(os.path.join(path , "contornos_" + str(Teste) + ".png"),img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    vetor()
                    break
            break
    return a
if a == 0:
    a = processo()

#https://visionproject.netlify.app
