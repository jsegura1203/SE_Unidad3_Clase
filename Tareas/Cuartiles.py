import numpy as n

#archivo = open("wine.csv")
#archivo = open("iris_completa.csv")
#archivo = open("instancia_clase.csv")
archivo = open("breast-cancer-wisconsin.csv")
contenido = archivo.readlines()

lectura = []
for i in contenido:
    lectura.append(i.split(","))

del lectura[0]

instancia = [ list(map(float,x[:len(x)-1])) for x in lectura ]

pos=[]

for i in range(3):
    pos.append(((i+1)*(len(instancia)+1))/4)

instancia=n.array(instancia)
for i in range(instancia.shape[1]):
    aux=instancia[:,i].copy()
    aux.sort()
    Q=[]
    for j in range(3):
        n=int(pos[j])
        Q.append(aux[n+1]+((pos[j]-n)*(aux[n+2]-aux[n+1])))
    print(Q)
    print("Rango intercuartil "+str(Q[2]-Q[0])+"\n")

