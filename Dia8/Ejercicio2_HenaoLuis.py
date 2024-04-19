tupla= ("banano",0.45,6, "manzana",4.55,2, "Piña",0.15,23) #esta es una tupla con las frutas, precios y cantidades
ListaTupla= [("banano",0.45,5,), ("manzana",4.55,25,), ("Piña",0.15,15)] #esta es una lista con las tuplas de las frutas, precios y cantidades
lista=list(tupla) #aca se pasa lo que hay en la dupla a la lista 
a=[]#aca se agregan los nomres en mayuscula
for i in range(0,len(lista),3):
    a.append(lista[i].upper())#se miran cada uno de los nombres y se pasan a mayusculas y se guardan en la lista a
print("Punto A")
print(a)

b=[]#aca se guardan los nombres de las frutas que valen menos de 0.50
for x in range(1,len(lista),3):
    if lista[x]<0.50: #se miran cada uno de los precios y si es menor a 0.50 se agregan los nombres en la lista b
        b.append(lista[x-1])
        
print("punto b\n",b)

c=[]#aca se guardan las cantidades de las frutas 
for y in range(2,len(lista),3):
    c.append(lista[y])#se miran cada una de las cantidades de las frutas y se guardan en la lista c
xd=c.index(max(c)) #con esto se usa el index para saber el lugar de la cantidad de fruta con mayor valor y se guarda en xd para saber cual es la cantidad de fruta con mayor valor se usa la funcion max en la lista c
print("punto c")
print(ListaTupla[xd]) #se muestra la tupla que hay en el puesto de c que esta guardado en la variable xd la tupla esta guradada en listatupla

d=[]#aca se van a guardar las cantidades por el precio de las frutas 
for z in range(1,len(lista),3):
    d.append(lista[z]*lista[z+1])# se miran cada una de los precios y cantidades de las frutas y se multiplican y se guardan en la lista b
print("punto d precio por cantidad ordenado de manera decreciente")
print(sorted(d,reverse=True)) #se usa sorted para ordenar la lista d y se usa el reverse=true para ordenarlos de manera descendente y luego se muestran en pantalla


#Desarrollado por Luis Orlando Henao Bermon c.c.1093904929 