from unittest import result
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from time import time

#Restantes es la lista de la longitud restante si coincide
restante = []

#String dado
e = "TAACGGATTGGATTACTGAGTAAATCGGAAAAGCACCCGGTTGAAACCCCGTCCCCTAAAAATCCCGTTTGCCCTTTTTTTCTTTAAAAAAAAAAAAAATATTAATTAAAAAAATTTAAT"
a = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"

#Contador es el numero de b's que coinciden al menos una vez con a
contador = 0


#Lista de string que nos pasan
filename = 's_3_sequence_1M.txt'
filename2 = 'tdt4287-unknown-adapter.txt'

time_list = []

def main():

    g = 0
    with open (filename2) as f_obj:
        for linea in f_obj:
            #1 for
            posiciones = charposition(linea, e)
            #1 for and 1 while
            comparar(e, linea, posiciones)                

    conteo = Counter(restante)
    print(contador)

    Limpio={}
    for clave in conteo:  
        valor=conteo[clave]
        if valor != 1:
            Limpio[clave] = valor
    llaves = Limpio.keys()
    llaves_limpias = sorted(llaves)
    sorted_limpio = {}
    for key in llaves_limpias:
        sorted_limpio[key] = Limpio[key]
   

    print(sorted_limpio.values())
    lists = sorted(sorted_limpio.items()) # sorted by key, return a list of tuples
    print("Longitud restante - numero de casos")
    print(lists)
    x, y = zip(*lists) # unpack a list of pairs into two tuples
    print(lists[0])

    plt.plot(x, y)
    plt.xlabel('Task 1: Length after match removal')
    plt.ylabel('Ocurrences')
    plt.title('Task 1 - Perfectly matching adapter fragments')
    plt.show()


#Funcion que segun va encontrando letra que coincide con el inicio de a,
#  mira a ver si coincide con un porcentaje de error
def charposition(string, a):
    char = a[0]
    pos = [] #list to store positions for each 'char' in 'string'
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos




def comparar(a, b, posiciones):

    resultado = 0
    tam = len(b) -1

    for i in posiciones:

        auxA = 0
        auxB = i

        while(auxB < tam):
            if(a[auxA] == b[auxB]):
                auxA +=1
                auxB +=1
                resultado +=1   
                continue
            if (auxA > 0):
                resultado = 0
                auxA = 0
                continue
            auxB +=1
            resultado = 0
        
        if(resultado > 0):
            break

    restante.append(tam-resultado)

    if (resultado > 0):
          global contador 
          contador += 1


main()