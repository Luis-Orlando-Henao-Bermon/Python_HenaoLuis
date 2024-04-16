
datos_crudos = input()
lista_datos = [int(d) for d in datos_crudos.split()]
numsuma=int(input())
for i in range(len(lista_datos)):
    restante=numsuma-lista_datos[i]
    for a in range(len(lista_datos)):
        if lista_datos[a]==restante:
            print(lista_datos[a])
           