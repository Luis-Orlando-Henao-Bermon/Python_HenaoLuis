from os import system
def menu():
    print("----------Menu----------\nPrecio de la subscripcion:50\n1. Mostrar saldo de la cuenta\n2. Recargar saldo de la cuenta\n3. Comprar suscripcion\n4. Comprar suscripcion para regalar\n5. Mostrar suscripciones\n6. Salir del programa")

menu()
opcion=int(input("Elige una opcion\n"))
precioSuscripcion=50
saldoCuenta=0


usuarioSub={}
usuarioSubRegalo={}

bol=True
while bol==True:
    if opcion==1:
        system("cls")
        print("El saldo de su cuenta es:",saldoCuenta)
        menu()
        opcion=int(input("Elige una opcion\n"))

    if opcion==2:
        system("cls")
        recarga=int(input("¿Cuanto deseas recargar?\n"))
        saldoCuenta=saldoCuenta+recarga
        menu()
        opcion=int(input("Elige una opcion\n"))

    if opcion==3:
        system("cls")
        
        cantidadSuscripcion=int(input("¿Cuantas suscripciones deseas comprar?\n"))
        while cantidadSuscripcion<1:
            print("Tienes que ingresar una cantidad mayor a 1")
            cantidadSuscripcion=int(input())
            
        if cantidadSuscripcion*precioSuscripcion>saldoCuenta:
            print("Saldo de cuenta insuficiente")
            menu()
            opcion=int(input("Elige una opcion\n"))
        else:
            saldoCuenta=saldoCuenta-cantidadSuscripcion*precioSuscripcion
            nombreSuscripcion=(input("Ingrese su nombre\n"))
            if cantidadSuscripcion>1:

                añoSuscripcion= []

                for i in range(cantidadSuscripcion):
                    print("Ingrese el año para la",i+1,"suscripcion")
                    añosub=int(input())
                    
                    while añosub<1990 or añosub>2020:
                        añosub=int(input("Por favor ingrese un año entre el 1990 y 2020\n"))

                    añoSuscripcion.append(añosub)
                usuarioSub[nombreSuscripcion]=añoSuscripcion
                menu()
                opcion=int(input("Elige una opcion\n"))
            elif cantidadSuscripcion==1:

                añoSuscripcion= []
                print("Ingrese el año para la suscripcion")
                añosub=int(input())

                while añosub<1990 or añosub>2020:
                    añosub=int(input("Por favor ingrese un año entre el 1990 y 2020\n"))

                añoSuscripcion.append(añosub)
                usuarioSub[nombreSuscripcion]=añoSuscripcion

                menu()
                opcion=int(input("Elige una opcion\n"))

    if opcion==4:
        system("cls")
        
        cantidadSuscripcion=int(input("¿Cuantas suscripciones deseas regalar?\n"))
        while cantidadSuscripcion<1:
            print("Tienes que ingresar una cantidad mayor a 1")
            cantidadSuscripcion=int(input())
            
        if cantidadSuscripcion*precioSuscripcion>saldoCuenta:
            print("Saldo de cuenta insuficiente")
            menu()
            opcion=int(input("Elige una opcion\n"))
        else:
            saldoCuenta=saldoCuenta-cantidadSuscripcion*precioSuscripcion
            nombreSuscripcion=(input("Ingrese el nombre de la persona a la que se lo quieres regalar\n"))
            if cantidadSuscripcion>1:
                añoSuscripcion= []
                for i in range(cantidadSuscripcion):
                    print("Ingrese el año para la",i+1,"suscripcion")
                    añosub=int(input())

                    while añosub<1990 or añosub>2020:
                        añosub=int(input("Por favor ingrese un año entre el 1990 y 2020\n"))

                    añoSuscripcion.append(añosub)
                usuarioSubRegalo[nombreSuscripcion]=añoSuscripcion
                menu()
                opcion=int(input("Elige una opcion\n"))

            elif cantidadSuscripcion==1:

                añoSuscripcion= []

                print("Ingrese el año para la suscripcion")
                añosub=int(input())

                while añosub<1990 or añosub>2020:
                    añosub=int(input("Por favor ingrese un año entre el 1990 y 2020\n"))

                añoSuscripcion.append(añosub)
                usuarioSubRegalo[nombreSuscripcion]=añoSuscripcion
                menu()
                opcion=int(input("Elige una opcion\n"))

    if opcion==5:
        print("Subscripciones usuario\nUsuario------Años de subscripcion")
        for a,b in usuarioSub.items():
            print(a,b)
        
        print("Subscripciones de regalo\nUsuario------Años de subscripcion")
        for a,b in usuarioSubRegalo.items():
            print(a,b)
        menu()
        opcion=int(input("Elige una opcion\n"))

    if opcion==6:
        bol=False