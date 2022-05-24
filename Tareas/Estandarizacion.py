import numpy as n

archivo = open("wine.csv")
contenido = archivo.readlines()

lectura = []
for i in contenido:
    lectura.append(i.split(","))

del lectura[0]

instancia = [ list(map(float,x[:len(x)-1])) for x in lectura ]

estandarizacion = []

estandarizacion = n.array(instancia)

Xestandar=[]

for i in range (estandarizacion.shape[1]):
    desv=n.std(estandarizacion[:,i])
    prom=n.mean(estandarizacion[:,i])
    columna=[]
    for j in range (estandarizacion.shape[0]):
        columna.append((estandarizacion[j][i]-prom)/desv)
    Xestandar.append(columna)

Xestandar = n.array(Xestandar)
Xestandar = Xestandar.T

salida = open ("nuevo.csv","w")
for i in range(Xestandar.shape[0]):
    flag=True
    renglon=""
    for j in range(Xestandar.shape[1]):
        if(not(Xestandar[i][j]<=3 and Xestandar[i][j]>=-3)):
            flag=False
        else:
            renglon+=str(round(Xestandar[i][j],4))+","
    if(flag):
        renglon=renglon[:len(renglon)-1]
        salida.write(renglon+"\n")

salida.close()

