
datos_crudos = input() #primero se introducen los numeros de la lista y se leen en str
lista_datos = [int(d) for d in datos_crudos.split()] # se pasan los datos de datos_crudos de str a int y se guarda en lista_datos
x=len(lista_datos)#esto es para saber cuantos datos hay en la lista 
while x>300: #si hay mas de 300 datos en la lista le dice que ingreso muchos datos y le tiene que vuelva a ingresar la lista 
    
    print("Error ingresaste muchos numeros")
    datos_crudos = input()
    lista_datos = [int(d) for d in datos_crudos.split()]
    x=len(lista_datos)

    
listaResuelta= []
for reps in lista_datos:# se usa un bucle for para mirar todos los valores que hay en lista_datos
    if reps not in listaResuelta: #si un dato no esta en la lista vacia(listaResuelta) se agrega ahi y si ya esta se ignora
        listaResuelta.append(reps)

n= len(listaResuelta) #esto es para saber cuantos valores hay en listaResuelta
for i in range(n-1):#se usa el metodo burbuja para ordenar de manera descendente 
    for j in range(n-1-i):
        if listaResuelta[j]>listaResuelta[j+1]:
            listaResuelta[j], listaResuelta[j+1]= listaResuelta[j+1], listaResuelta[j]

print(listaResuelta) #finalmete se escribe la listaResuelta
#desarrollado por Luis Orlando Henao Bermon c.c.1093904929