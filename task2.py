from unittest import result
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from time import time

#Restantes es la lista de la longitud restante si coincide
restante = []

#String dado
a = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"


#Contador es el numero de b's que coinciden al menos una vez con a
contador = 0


#Lista de string que nos pasan
filename = 's_3_sequence_1M.txt'

def main():

    g = 0
    start_time = time()
    with open (filename) as f_obj:  
        for linea in f_obj:
            g += 1
            if(g==1):
                start_time = time()
            comparar(a, linea) 

            if(g==1000):
                tiempo_1000 = time() - start_time            

            if(g==100000):
                tiempo_100000 = time() - start_time

            if(g==1000000):
                tiempo_1000000 = time() - start_time                


    conteo = Counter(restante)  

    print(contador)
    print("tiempo_1000: %0.10f seconds." % tiempo_1000)
    print("tiempo_100000: %0.10f seconds." % tiempo_100000)
    print("tiempo_1000000: %0.10f seconds." % tiempo_1000000)

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
    print(lists[0])

    x, y = zip(*lists) # unpack a list of pairs into two tuples

    plt.plot(x, y)
    plt.xlabel('Length  after match removal')
    plt.ylabel('Ocurrences')
    plt.title('Task 2 - Length distrib')
    plt.show()

def comparar(a, b):

    tam = len(b)-1
    resultado = 0
    error = 0
    maxE = 0
    #Porcentaje de fallos permitidos
    #Para poner 0, poner un 1 (mismo resultado)
    valor = 25

    for i in range(tam):
        #print(i)
        maxE = ((tam-i)*valor)/100
        auxA = 0
        auxB = i

        #Hasta que b llegue al final y su error sea aceptable
        while((auxB < tam) and (error < maxE)):
            #Si son iguales, se pasa al siguiente
            if(a[auxA] == b[auxB]):
                auxA +=1
                auxB +=1
                resultado +=1
            #Si no, aumenta un error
            else:
                auxA +=1
                auxB +=1
                resultado +=1
                error += 1            
        
        if((error < maxE) and (resultado > 0)):
            #print(b[i:])
            break
        else:
            resultado = 0 
            error = 0

    restante.append(tam-resultado)

    if (resultado > 0):
        global contador 
        contador += 1



main()