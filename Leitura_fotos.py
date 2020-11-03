# Programa para realizar a leitura de todas as faces cadastradas


import os                                               
from cv2 import cv2                                              
import numpy as np                                      
from PIL import Image                                   


EigenFace = cv2.face.EigenFaceRecognizer_create(15)             # Cria um identificador EIGEN FACE  

path = 'Faces_cadastro'                                         # Pasta onde se encontram as fotos para leitura
def getImageWithID (path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    FaceList = []
    IDs = []
    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')          # Abre a imagem e converte para preto e branco
        faceImage = faceImage.resize((110,110))                 # Redimensiona a imagem para assim, o EIGEN conseguir "treinar"
        faceNP = np.array(faceImage, 'uint8')                   # Converte a imagem para um vetor Numpy
        ID = int(os.path.split(imagePath)[-1].split('.')[1])    # Encontra o ID no vetor das fotos
        FaceList.append(faceNP)                                 # Insere o vetor Numpy na lista
        IDs.append(ID)                                          # Insere o ID na lista de IDs
        cv2.imshow('Faces para "treinamento"', faceNP)                      # Mostra as imagens da lista
        cv2.waitKey(1)
    return np.array(IDs), FaceList                              # Os IDs são convertidos em um vetor Numpy
IDs, FaceList = getImageWithID(path)

# "Treinamento" do identificador
print('Treinando...')
EigenFace.train(FaceList, IDs)                                  # O identificador é "treinado" usando as imagens
print('Reconhecimento EIGEN FACE completo!')
EigenFace.save('Recogniser/trainingDataEigan.xml')
print('Arquivo .xml salvo!')


cv2.destroyAllWindows()
