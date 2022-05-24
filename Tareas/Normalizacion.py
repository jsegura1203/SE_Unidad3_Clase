import numpy as n

archivo = open("iris_completa.csv")
contenido = archivo.readlines()

lectura = []
for i in contenido:
    lectura.append(i.split(","))
encabezados = lectura[0]
del lectura[0]

instancia = [ list(map(float,x[:len(x)-1])) for x in lectura ]

normalizacion = []

instancia = n.array(instancia)

for j in range(len(instancia[0])):
    columna=[]
    min= n.min(instancia[:, j])
    max=n.max(instancia[:, j])
    for i in range (len(lectura)):
        columna.append(round((instancia[i][j]-min)/(max-min),3))
    normalizacion.append(columna)

normalizacion = n.array(normalizacion)
normalizacion= normalizacion.T

complemento = []

for i in range (len(lectura)):
    linea=[]
    for j in range (len(instancia[0])):
        linea.append(round(1-normalizacion[i][j],3))
    complemento.append(linea)

print("Normalizacion")

for i in normalizacion:
    print(i)

print("\nComplemento")
for i in complemento:
    print(i)


