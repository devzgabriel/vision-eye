#Programa para realizar a leitura dos nomes e cadastrá-los
#8e6fa624
from cv2 import cv2  
import math 
import time 
import os 
import requests
import urllib, json
import json
#6622ea45
now_time = time.perf_counter

face = cv2.CascadeClassifier(r'C:\Users\Pedro\Desktop\Vision\Haar\haarcascade_frontalcatface.xml') 
glass_cas = cv2.CascadeClassifier(r'C:\Users\Pedro\Desktop\Vision\Haar\haarcascade_eye_tree_eyeglasses.xml') 
WHITE = [255, 255, 255]

NAME = []
CARGO = []
ID = []
code = []
status = []
url = "https://server-vision.herokuapp.com/sessions"
headers = {"Content-Type":"application/json"}
y = 0
while True:
        def empresa():
                print('\n')
                print('=====================================')
                print('====== Identificacao da empresa =====')
                print('=====================================\n')
                n = input("-> Insira o ID da empresa: ")
                pload = {"id":n}
                x = requests.post(url = url, headers = headers, json = pload)
                to_json = json.loads(x.text)
                s = input("-> Sua empresa é a " + to_json["name"] + "? s/n: ")
                return s, n
        S, O = empresa()
        def FileRead():
                url1 = "https://server-vision.herokuapp.com/workers"
                headers1 = {"Authorization": O}
                pload = {"id":O}
                x1 = requests.get(url = url1, headers = headers1, json = pload)
                to_json = json.loads(x1.text)
                y = 1
                Laststring = len(to_json)
                for i in range(len(to_json)):
                    NAME.append(to_json[i]["name"])
                    CARGO.append(to_json[i]["occupation"])
                    ID.append (to_json[i]["code"])
                    code.append(to_json[i]["id"])
                    status.append(to_json[i]["status"])
                print('\n')
                print('=====================================')
                print('====== Identificacao concluida ======')
                print('=====================================')
                return NAME, CARGO, Laststring, ID, code, status, O, y      # Retorna os nomes cadastrados
        if S == "s":
                Names, Cargos, laststring, iD, CODE, STATUS, N, Y  = FileRead()
                break

        """Info = open("Cadastros.txt", "r")                   # Leitura do arquivo onde se encontram os nomes cadastrados
        NAME = []                                           
        while (True):                                       # Leitura de todas as linhas e armazenamento de nome
            Line = Info.readline()
            if Line == '':
                break
            teste1 = Line.index(",") + 2
            teste2 = Line.index("-") - 1

            NAME.append(Line[(teste1):(teste2)])"""


       



"""def FileRead2():
    Info = open("Cadastros.txt", "r")                   # Leitura do arquivo onde se encontram os cargos cadastrados
    CARGO = []                                          
    while (True):                                       # Leitura de todas as linhas e armazenamento de cargo
        Line = Info.readline()
        if Line == '':
            break
        teste3 = Line.index("-") + 2
        CARGO.append (Line[(teste3):-1])
        
       
        return CARGO"""                                       
def Nomes():
        Nomes = []
        IDs = []
        for i in range(len(Names)):
                Nomes.append(Names[i])
        for i in range(len(iD)):
                IDs.append(iD[i])
        return Nomes, IDs

# Função para encontrar o nome


"""def file_is_empty(path):
    return os.stat(path).st_size==0

with open('Cadastros.txt') as f:
    lines = f.readlines()
    if file_is_empty('Cadastros.txt'):
        last_string = 1
    else:
        last_row = lines[-1]
        string_last = last_row  
        for s in string_last.split(): 
            if s.isdigit():
                last_string = int(s) 
                print("A base possui: " + str(last_string) + " " + "pessoas" )"""


def ID2Name(ID,conf):
    if ID>=1 and ID <= laststring:
        NameString = Names[ID-1]                        # Encontra o nome usando o indíce do ID
    else:
        NameString = "Face desconhecida"  
    return NameString

def ID3Name(ID,conf):
    if ID>=1 and ID <= laststring:
        Cargo = Cargos[ID-1]                            # Encontra o cargo usando o indíce do ID
    else:
        Cargo = "Cargo desconhecido"  

    return Cargo

# Função para ler o arquivo e adicionar o nome cadastrado à sua última linha 


"""def AddName():

    repetido = 0
    
    Name = input('Digite seu nome: ')
    Info = open("Cadastros.txt", "r+")
    with open('Cadastros.txt') as f:
        for l_num, l in enumerate(f, 1):
            teste4 = l.index("-") - 1
            if(Name == l[4:teste4]):
                print("Nome repetido")
                repetido = 1
                break

        if(repetido == 0):
            Cargo = input('Digite seu cargo: ')
            ID = ((sum(1 for line in Info))+1)
            Info.write(str(ID) + " , " + Name + " - " + str(Cargo) + "\n")
            print ("Nome armazenado em " + str(ID))
            Info.close()
            return ID
    
        if(repetido == 1):
            AddName()
"""
# Desenha uma marcação ao redor da face, do nome e do cargo 


def DispID(x, y, w, h, NAME,Image):
 

    Name_y_pos = y - 10
    Name_X_pos = x + w/2 - (len(NAME)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10

    
    #draw_box(Image, x, y, w, h)
    
    #cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), (0,0,0), -2)              
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), (0,0,0), -2)
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), WHITE, 1)           
    cv2.putText(Image, NAME, (int(Name_X_pos), int(Name_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)                         

    
#def draw_box(Image, x, y, w, h):
    #cv2.line(Image, (x, y), (x + (int(w/5)) ,y), WHITE, 2)
    #cv2.line(Image, (x+((int(w/5)*4)), y), (x+w, y), WHITE, 2)
    #cv2.line(Image, (x, y), (x, y+(int(h/5))), WHITE, 2)
    #cv2.line(Image, (x+w, y), (x+w, y+int((h/5))), WHITE, 2)
    #cv2.line(Image, (x, (y+int((h/5*4)))), (x, y+h), WHITE, 2)
    #cv2.line(Image, (x, (y+h)), (x + int((w/5)) ,y+h), WHITE, 2)
    #cv2.line(Image, (x+(int((w/5)*4)), y+h), (x + w, y + h), WHITE, 2)
    #cv2.line(Image, (x+w, (y+int((h/5*4)))), (x+w, y+h), WHITE, 2)



def DispID2(x, y, w, h, Cargo, Image):

      

    CARGO_y_pos = y + 275
    CARGO_X_pos = x + w/2 - (len(Cargo)*7/2)

    if CARGO_X_pos < 0:
       CARGO_X_pos = 0
    elif (CARGO_X_pos +10 + (len(Cargo) * 7) > Image.shape[1]):
         CARGO_X_pos= CARGO_X_pos - (CARGO_X_pos +10 + (len(Cargo) * 7) - (Image.shape[1]))
    if CARGO_y_pos > 265:
        CARGO_y_pos = CARGO_y_pos = y + h + 25

    cv2.rectangle(Image, (int(CARGO_X_pos-10), int(CARGO_y_pos-25)),(int(CARGO_X_pos +10 + (len(Cargo) * 7)), int(CARGO_y_pos-1)), (0,0,0), -2)
    cv2.rectangle(Image, (int(CARGO_X_pos-10), int(CARGO_y_pos-25)),(int(CARGO_X_pos +10 + (len(Cargo) * 7)), int(CARGO_y_pos-1)), WHITE, 1)     
    cv2.putText(Image, Cargo, (int(CARGO_X_pos), int(CARGO_y_pos -10)), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)


def DispID3(x, y, w, h, NAME, Image):

     

    Name_y_pos = y - 70
    Name_X_pos = x + w/2 - (len(NAME)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(NAME) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos > 0:
        Name_y_pos = Name_y_pos = y + h + 10
          

    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), (0,0,0), -2)
    cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), WHITE, 1)          
    cv2.putText(Image, NAME, (int(Name_X_pos), int(Name_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)                         


def DrawBox(Image, x, y, w, h):
    cv2.rectangle(Image, (x, y), (x + w, y + h), (255, 255, 255), 1)     





def DetectEyes(Image):
    Theta = 0
    rows, cols = Image.shape
    glass = glass_cas.detectMultiScale(Image)                                               
    for (sx, sy, sw, sh) in glass:
        if glass.shape[0] == 2:                                                            
            if glass[1][0] > glass[0][0]:
                DY = ((glass[1][1] + glass[1][3] / 2) - (glass[0][1] + glass[0][3] / 2))    
                DX = ((glass[1][0] + glass[1][2] / 2) - glass[0][0] + (glass[0][2] / 2))    
            else:
                DY = (-(glass[1][1] + glass[1][3] / 2) + (glass[0][1] + glass[0][3] / 2))   
                DX = (-(glass[1][0] + glass[1][2] / 2) + glass[0][0] + (glass[0][2] / 2))   

            if (DX != 0.0) and (DY != 0.0):                                                 
                Theta = math.degrees(math.atan(round(float(DY) / float(DX), 2)))            
                #print ("Theta  " + str(Theta))

                M = cv2.getRotationMatrix2D((cols / 2, rows / 2), Theta, 1)                 
                Image = cv2.warpAffine(Image, M, (cols, rows))
                # cv2.imshow('ROTATED', Image)                                              

                Face2 = face.detectMultiScale(Image, 1.3, 5)                                
                for (FaceX, FaceY, FaceWidth, FaceHeight) in Face2:
                    CroppedFace = Image[FaceY: FaceY + FaceHeight, FaceX: FaceX + FaceWidth]
                    return CroppedFace


def tell_time_passed():
    print ('TIME PASSED ' + str(round(((time.perf_counter() - now_time)/60), 2)) + ' MINS')


