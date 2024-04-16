
datos_crudos = input()
lista_datos = [int(d) for d in datos_crudos.split()]
x=len(lista_datos)
while x>300:
    
    print("Error ingresaste muchos numeros")
    datos_crudos = input()
    lista_datos = [int(d) for d in datos_crudos.split()]
    x=len(lista_datos)

    
listaResuelta= []
for reps in lista_datos:
    if reps not in listaResuelta:
        listaResuelta.append(reps)

n= len(listaResuelta)
for i in range(n-1):
    for j in range(n-1-i):
        if listaResuelta[j]>listaResuelta[j+1]:
            listaResuelta[j], listaResuelta[j+1]= listaResuelta[j+1], listaResuelta[j]

print(listaResuelta)