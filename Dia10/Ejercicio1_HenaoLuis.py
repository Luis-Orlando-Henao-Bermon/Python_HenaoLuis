import json #se importa json para poder leer la lista
inputx=input("Entrada 1 = ") #en una variable se lee la lista (tiene que estar escrita como si estuviera dentro del codigo ejemplo: [1,3,5,9])
objetivo=int(input()) #se lee el objetivo que se quiere saber si esta en la lista 
lista=json.loads(inputx) #se usa el json.loads para pasar de un json(inpux) a la lista (basicamente un json es un texto pero con el formato de la lista, diccionario o tupla)

if objetivo in lista: #si el objetivo esta en la lista le muestra la pocicion que se hace con el index
    print(lista.index(objetivo))

#si el objeivo no esta en la lista se agrega a la lista y se crea una nueva lista con el objetivo añadido la nueva lista se 
#crea ordenada de una vez luego se escribe la pocicion de el objetivo en la lista ya ordenada 

if objetivo not in lista: 
    lista.append(objetivo)
    lista1=sorted(lista)
    print(lista1.index(objetivo))

inputx=input("Entrada 2 = ")
objetivo=int(input())
lista=json.loads(inputx)

if objetivo in lista:#si el objetivo esta en la lista le muestra la pocicion que se hace con el index
    print(lista.index(objetivo))

#si el objeivo no esta en la lista se agrega a la lista y se crea una nueva lista con el objetivo añadido la nueva lista se 
#crea ordenada de una vez luego se escribe la pocicion de el objetivo en la lista ya ordenada 
if objetivo not in lista:
    lista.append(objetivo)
    lista1=sorted(lista)
    print(lista1.index(objetivo))

inputx=input("Entrada 3 = ")
objetivo=int(input())
lista=json.loads(inputx)

if objetivo in lista:#si el objetivo esta en la lista le muestra la pocicion que se hace con el index
    print(lista.index(objetivo))

#si el objeivo no esta en la lista se agrega a la lista y se crea una nueva lista con el objetivo añadido la nueva lista se 
#crea ordenada de una vez luego se escribe la pocicion de el objetivo en la lista ya ordenada 
if objetivo not in lista:
    lista.append(objetivo)
    lista1=sorted(lista)
    print(lista1.index(objetivo))

#desarrollado por Luis Henao c.c. 1093904929
