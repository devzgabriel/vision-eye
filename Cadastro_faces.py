#Programa utilizado para realizar o cadastro de um funcionário

from cv2 import cv2

import numpy as np

import Identificador_nomes

from Identificador_nomes import Names
from Identificador_nomes import Cargos
from Identificador_nomes import iD
 
import requests

import urllib, json

import json


def func():
    confirm1 = 0
    confirm2 = 0
    confirm3 = 0
    print("\n")
    print('=====================================')
    print('==== Identificacao do funcionario ===')
    print('=====================================\n')
    verif1 = input("Digite seu nome: ")
    verif2 = input("Digite seu código: ")
    verif3 = input("Digite seu ocupação: ")
    print("\n\n")
    for i in range(len(Names)):
        if verif1 == Names[i]:
            confirm1 = 1
    for i in range(len(iD)):
        if verif2 == iD[i]:
            confirm2 = 1
    for i in range(len(Cargos)):
        if verif3 == Cargos[i]:
            confirm3 = 1  
        #9d2969dd

    if confirm1 == 1 and confirm2 == 1 and  confirm3 == 1:
        WHITE = [255, 255, 255]


        #importa os arquivos .xml para realizar a detecção da face

        face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml') 
        eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml') 

        ID = verif2
        Count = 0
        cap = cv2.VideoCapture(0)                                                                           # Habilita a câmera

        print('\n=====================================')
        print('========= Captura das fotos =========')
        print('=====================================\n')

        while Count < 50:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                                    # Imagem da câmera em preto e branco
            if np.average(gray) > 110:                                                                      # Definindo o brilho  
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)                                         # Detecta as faces e armazena as posições 
                for (x, y, w, h) in faces:                                                                  # Define as dimensões da face detectada
                    FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]    # A face é recortada 
                    Img = (Identificador_nomes.DetectEyes(FaceImage))
                    cv2.putText(gray, "Face identificada", (x+int((w/2)), y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
                    if Img is not None:
                        frame = Img                                                                         # Mostra as faces detectadas
                    else:
                        frame = gray[y: y+h, x: x+w]
                    cv2.imwrite("Faces_cadastro/" + str(verif1) + "." + str(ID) + "." + str(Count) + ".jpg", frame)
                    cv2.waitKey(300)
                    cv2.imshow("Foto capturada", frame)                                                     # Mostra a imagem da face capturada
                    Count = Count + 1
                    print('Foto #' + str(Count))
            cv2.imshow('Captura de faces do cadrastro', gray)                                               # Mostra o vídeo o qual está se capturando as faces
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        print('\n===================================')
        print('===== Captura da face concluida =====')
        print('=====================================\n')
        cap.release()
        cv2.destroyAllWindows()
    else:
        print('\n==========================================')
        print("Insira os dados corretamente ou cadastre-se!")
        print('============================================\n')
        func()
func()
