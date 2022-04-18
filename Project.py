import os
import shutil


name=[]
listauni=[]

caminho = input('Digite o caminho \n')

caminho = caminho + "\ "

caminho = caminho[:-1]
caminhorig = caminho[:-1]

i=0

numchar = int(input('Digite o número de caracteres\n'))

#read de files in directory
for file in os.listdir(caminho):
        name.append(str(file))        

#pegando apenas os primeiros charac 
for nome in name:
        name[i] = nome[:numchar]
        i=i+1

#create a list with no dupplicate values
listauni = list(set(name))


#create directories

for a in listauni:
        caminhodest = caminho + a
        os.mkdir(caminhodest)

        for arquivo in os.listdir(caminho):
                if arquivo[:numchar] == a:
                        shutil.move(caminho+arquivo, caminhodest)          
                        

    
