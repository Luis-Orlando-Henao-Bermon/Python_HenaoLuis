import json 
from os import system

def menu():
    print("-------Menu-------\n1. Mostrar todos los eventos que hay\n2. Eliminar evento\n3. Modificar evento\n4. Crear evento\n5. Salir del programa")


#se abre el archivo poniendo el nombre del archivo y se usa encoding="utf-8" para que codifique lo que esta en large-file.json y luego se pasa esto a (datos) convirtiendola en lista
with open("large-file.json", encoding="utf-8") as arcrivo:
    datos=json.load(arcrivo)

TipoEvento=[]#en esta lista se guardaran los eventos que hayan 
for i in range(len(datos)): #se usa un bucle for para leer todos los datos que hayan en la lista(datos)
    if datos[i]["type"]not in TipoEvento: #si un tipo de evento no esta en la lista (TipoEvento) se agrega al final para que se guarden todos los diferentes tipos de eventos
        TipoEvento.append(datos[i]["type"])

def eventos():
    for a in range(len(TipoEvento)): # esto solo es un bucle para que muestre los eventos que hay en forma vertical
        print(TipoEvento[a])

menu() #se muestra el menu y se pide que escoja una opcion
opcion=int(input("Elige una opcion\n"))
bol=True
while bol==True:
    if opcion==1: #esta es la opcion de mostrar los eventos que hay 
        system("clear")#se limpia pantalla
        print("-----Eventos-----")
        eventos()#Se mustran los eventos que hay 
        menu()#se muestra el menu y se pide que escoja una opcion
        opcion=int(input("Elige una opcion\n"))

    elif opcion==2:
        system("clear")#se limpia pantalla

        print("-----Eventos-----")
        eventos()#se muestran los eventos  que hay y le pregunta cual desea eliminar

        eventoEliminar=input("¿Que evento deseas eliminar?\n")
        bol2=True
        while bol2==True:#se usa un bucle while para que cada vez que el evento que ingrese el ususario no este en la lista le pida que ingrese uno de los que hayan
            if eventoEliminar not in TipoEvento:#si el evento no esta en la lista Le pide que ingrese un evento de los que hay ahi
                eventoEliminar=input("Ingrese un evento de los que hay en la lista\n")
            else:
                bol2=False#si el evento ingresado por el usuario esta en la lista se termina el bucle while 

        TipoEvento.remove(eventoEliminar)#despues de ver que el evento esta en la lita se elimina con .remove
        menu() #se muestra el menu y se pide que escoja una opcion
        opcion=int(input("Elige una opcion\n"))

    elif opcion==3:
        system("clear")
        print("-----Eventos-----")
        eventos()#se muestran los eventos que hay y le pregunta cual desea modificar
        eventoModificar=input("¿Que evento deseas modificar?\n")
        bol3=True
        while bol3==True:#se usa un bucle while para que cada vez que el evento que ingrese el ususario no este en la lista le pida que ingrese uno de los que hayan
            if eventoModificar not in TipoEvento:#si el evento no esta en la lista Le pide que ingrese un evento de los que hay ahi
                eventoModificar=input("Ingrese un evento de los que hay en la lista\n")
            else:
                bol3=False#si el evento ingresado por el usuario esta en la lista se termina el bucle while

        modificacion=input("¿como se va a llamar ahora ese evento?\n")#despues de ver que el evento ingresado por el usuario este en la lista  le pregunta como quiere que se llame ahora ese evento
        for x in range(len(TipoEvento)):#se usa un bucle for para que lea todo lo que haya en la lista TipoEvento(es la lista en donde estan todos los eventos)
            if TipoEvento[x]==eventoModificar:# si el evento de la lista en la pocicion x (la posicion x pasa por cada uno de los datos en TipoEvento)es igual al ingresado por el ususario modifica lo que haya en la pocicion en la que estan actualemte por Modificacion(es como el usuario dijo que se va a llamar ahora ese evento) 
                TipoEvento[x]=modificacion
            
        menu()#se muestra el menu y se pide que escoja una opcion
        opcion=int(input("Elige una opcion\n"))
    elif opcion==4:
        #se pide el nombre del nuevo evento y se añade al final de la lista TipoEvento
        EventoAñadir=input("¿Como se va a llamar el evento que quieres añadir?\n")   
        TipoEvento.append(EventoAñadir) 
        menu()#se muestra el menu y se pide que escoja una opcion
        opcion=int(input("Elige una opcion\n"))
    elif opcion==5:
        print("Gracias por usar el programa")
        bol=False
#desarrollado por Luis Henao c.c. 1093904929