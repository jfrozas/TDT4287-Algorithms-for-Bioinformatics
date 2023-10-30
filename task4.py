filename = 'tdt4287-unknown-adapter.txt'
filename2 = 's_3_sequence_1M.txt'
filename3 = 'seqset3.txt'

listaA = [0] * 120
listaT = [0] * 120
listaC = [0] * 120
listaG = [0] * 120


def main():
    a = 0
    with open (filename3) as f_obj:
        for linea in f_obj: 
            a += 1 
            print(a)
            oplinea(linea)

    str = ""

    for i in range(len(listaA)):
        print("\n")
        print("  a      t      c     g ")
        print(listaA[i], listaT[i], listaC[i], listaG[i])
        
        maxnumber = max(listaA[i], listaT[i], listaC[i], listaG[i])
        if (listaA[i] == maxnumber and listaA[i] != 0):
            str += "A"
        if (listaT[i] == maxnumber and listaT[i] != 0):
            str += "T"           
        if (listaC[i] == maxnumber and listaC[i] != 0):
            str += "C"
        if (listaG[i] == maxnumber and listaG[i] != 0):
            str += "G" 

    
    print("\nAdapter Sequence and posible changes")
    print(str)



def oplinea(a):

    for i in range(len(a[:-1])):
        #print(i, linea[i])
        if (a[i] == "A"):
            listaA[i] += 1
        if (a[i] == "T"):
            listaT[i] += 1
        if (a[i] == "C"):
            listaC[i] += 1                                    
        if (a[i] == "G"):
            listaG[i] += 1  

main()