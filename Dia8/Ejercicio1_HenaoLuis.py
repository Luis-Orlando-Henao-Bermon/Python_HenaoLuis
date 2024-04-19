from os import system
def menu(): #funcion para mostrar el menu
    print("----------Menu----------\nPrecio de la subscripcion:50\n1. Mostrar saldo de la cuenta\n2. Recargar saldo de la cuenta\n3. Comprar suscripcion\n4. Comprar suscripcion para regalar\n5. Mostrar suscripciones\n6. Salir del programa")

menu()#se llama el menu y se lee la opcion a escoger 
opcion=int(input("Elige una opcion\n"))
precioSuscripcion=50 #este es el precio de la suscripcion
saldoCuenta=0#este es el saldo de la cuenta que inicialmente es 0 


usuarioSub={}#este es el arreglo que se usa para guardar las suscripciones del la opcion 3
usuarioSubRegalo={}#este es el arreglo que se usa para guardar las suscripciones del la opcion 4

bol=True
while bol==True:
    if opcion==1: #si ecoge la opcion 1 se limpia pantalla y se muestra el saldo de la cuenta 
        system("cls")
        print("El saldo de su cuenta es:",saldoCuenta)
        menu()#se vuelve a mostrar el menu y se leen las opciones para poder cambiar entre opciones
        opcion=int(input("Elige una opcion\n"))

    if opcion==2:#si escoge la opcion 2 se limpia pantalla y se suma la cantidad que quiere agregar al saldo actual
        system("cls")
        recarga=int(input("¿Cuanto deseas recargar?\n"))
        saldoCuenta=saldoCuenta+recarga
        menu()#se vuelve a mostrar el menu y se leen las opciones para poder cambiar entre opciones
        opcion=int(input("Elige una opcion\n"))

    if opcion==3:
        system("cls")
        
        cantidadSuscripcion=int(input("¿Cuantas suscripciones deseas comprar?\n"))#primero se pregunta cuantas suscripciones quiere
        while cantidadSuscripcion<1:# si ingresa una cantidad negativa le dice que tiene que ingresar una cantidad positiva 
            print("Tienes que ingresar una cantidad positiva")
            cantidadSuscripcion=int(input())
            
        if cantidadSuscripcion*precioSuscripcion>=saldoCuenta:#se mira si la cantidad que de suscripciones que quiere por el precio es mayor al saldo actual, si es mayor le manda error de saldo insuficiente y lo vuelve a mandar al menu, si es menor continua el codigo
            print("Saldo de cuenta insuficiente")
            menu()#se vuelve a mostrar el menu y se leen las opciones para poder cambiar entre opciones
            opcion=int(input("Elige una opcion\n"))
        else:#si la canidad de suscripciones por el precio de suscripcion es menor o igual al saldo actual se le resta eso al saldo actual
            saldoCuenta=saldoCuenta-cantidadSuscripcion*precioSuscripcion
            nombreSuscripcion=(input("Ingrese su nombre\n")) #se pide el nombre del que esta adquiriendo la suscripcion
            if cantidadSuscripcion>1: #si la cantidad de suscripciones es mayor a 1 se usa un bucle for para que le pida los años en base a la cantidad de suscripciones

                añoSuscripcion= [] #se crea una lista vacia para poner los años de las suscripciones

                for i in range(cantidadSuscripcion): #con el bucle for se piden los años en base a la cantidad de suscripciones y se guardan en la lista de añosuscripcion
                    print("Ingrese el año para la",i+1,"suscripcion")
                    añosub=int(input())
                    
                    while añosub<1990 or añosub>2020: #mientras el año ingresado sea menor a 1990 o mayor a 2020 le pide que ingrese un año en ese rango
                        añosub=int(input("Por favor ingrese un año entre el 1990 y 2020\n"))

                    añoSuscripcion.append(añosub) #aca se añaden los años a la lista de los años 
                usuarioSub[nombreSuscripcion]=añoSuscripcion # se crea un diccionario con base al nombre del usuario y se le agregan los valores de los años de suscripciones esto se guarda en usuarioSub
                menu()#se vuelve a mostrar el menu y se leen las opciones para poder cambiar entre opciones
                opcion=int(input("Elige una opcion\n"))
            elif cantidadSuscripcion==1:# si la cantidad de las suscripciones es 1 sola se hace lo mismo que en el caso de que sean mas de una solo que no se usa el bucle for y se pregunta por un solo año

                añoSuscripcion= []
                print("Ingrese el año para la suscripcion")
                añosub=int(input())

                while añosub<1990 or añosub>2020:
                    añosub=int(input("Por favor ingrese un año entre el 1990 y 2020\n"))

                añoSuscripcion.append(añosub)
                usuarioSub[nombreSuscripcion]=añoSuscripcion

                menu()#se vuelve a mostrar el menu y se leen las opciones para poder cambiar entre opciones
                opcion=int(input("Elige una opcion\n"))

    if opcion==4:
        system("cls")
        
        cantidadSuscripcion=int(input("¿Cuantas suscripciones deseas comprar?\n"))#primero se pregunta cuantas suscripciones quiere
        while cantidadSuscripcion<1:# si ingresa una cantidad negativa le dice que tiene que ingresar una cantidad positiva 
            print("Tienes que ingresar una cantidad positiva")
            cantidadSuscripcion=int(input())
            
        if cantidadSuscripcion*precioSuscripcion>=saldoCuenta:#se mira si la cantidad que de suscripciones que quiere por el precio es mayor al saldo actual, si es mayor le manda error de saldo insuficiente y lo vuelve a mandar al menu, si es menor continua el codigo
            print("Saldo de cuenta insuficiente")
            menu()#se vuelve a mostrar el menu y se leen las opciones para poder cambiar entre opciones
            opcion=int(input("Elige una opcion\n"))
        else:#si la canidad de suscripciones por el precio de suscripcion es menor o igual al saldo actual se le resta eso al saldo actual
            saldoCuenta=saldoCuenta-cantidadSuscripcion*precioSuscripcion
            nombreSuscripcion=(input("Ingrese su nombre\n")) #se pide el nombre del que esta adquiriendo la suscripcion
            if cantidadSuscripcion>1: #si la cantidad de suscripciones es mayor a 1 se usa un bucle for para que le pida los años en base a la cantidad de suscripciones

                añoSuscripcion= [] #se crea una lista vacia para poner los años de las suscripciones

                for i in range(cantidadSuscripcion): #con el bucle for se piden los años en base a la cantidad de suscripciones y se guardan en la lista de añosuscripcion
                    print("Ingrese el año para la",i+1,"suscripcion")
                    añosub=int(input())
                    
                    while añosub<1990 or añosub>2020: #mientras el año ingresado sea menor a 1990 o mayor a 2020 le pide que ingrese un año en ese rango
                        añosub=int(input("Por favor ingrese un año entre el 1990 y 2020\n"))

                    añoSuscripcion.append(añosub) #aca se añaden los años a la lista de los años 
                usuarioSubRegalo[nombreSuscripcion]=añoSuscripcion # se crea un diccionario con base al nombre del usuario al que le va a regalar las suscripciones y se le agregan los valores de los años de suscripciones esto se guarda en usuarioSubRegalo
                menu()#se vuelve a mostrar el menu y se leen las opciones para poder cambiar entre opciones
                opcion=int(input("Elige una opcion\n"))
            elif cantidadSuscripcion==1:# si la cantidad de las suscripciones es 1 sola se hace lo mismo que en el caso de que sean mas de una solo que no se usa el bucle for y se pregunta por un solo año

                añoSuscripcion= []
                print("Ingrese el año para la suscripcion")
                añosub=int(input())

                while añosub<1990 or añosub>2020:
                    añosub=int(input("Por favor ingrese un año entre el 1990 y 2020\n"))

                añoSuscripcion.append(añosub)
                usuarioSubRegalo[nombreSuscripcion]=añoSuscripcion

                menu()#se vuelve a mostrar el menu y se leen las opciones para poder cambiar entre opciones
                opcion=int(input("Elige una opcion\n"))

    if opcion==5:
        print("Subscripciones usuario\nUsuario------Años de subscripcion")
        for a,b in usuarioSub.items():#se usa este bucle for para escribir el usuario y el valor que serian los años de las suscriones en el diccionario de usuarioSub
            print(a,b)
        
        print("Subscripciones de regalo\nUsuario------Años de subscripcion")
        for a,b in usuarioSubRegalo.items():#se usa este bucle for para escribir el usuario al que le va a regalar las suscripciones y el valor que serian los años de las suscriones en el diccionario de usuarioSubRegalo
            print(a,b)
        menu()#se vuelve a mostrar el menu y se leen las opciones para poder cambiar entre opciones
        opcion=int(input("Elige una opcion\n"))

    if opcion==6:
        bol=False
#Desarrollado por Luis Orlando Henao Bermon c.c.1093904929