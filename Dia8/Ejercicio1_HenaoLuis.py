from os import system
def menu():
    print("----------Menu----------\n1. Mostrar saldo de la cuenta\n2. Recargar cuenta\n3. Comprar suscripcion\n4. Comprar suscripcion para regalar\n5. Mostrar suscripciones\n6. Salir del programa")

menu()
opcion=int(input("Elige una opcion\n"))
precioSuscripcion=50
saldoCuenta=0


añosub={}

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
                    
                    añoSuscripcion.append(int(input()))
                añosub[nombreSuscripcion]=añoSuscripcion
                print(añosub)
                menu()
                opcion=int(input("Elige una opcion\n"))
            elif cantidadSuscripcion==1:
                añoSuscripcion= []
                print("Ingrese el año para la suscripcion")
                añoSuscripcion.append(int(input()))
                añosub[nombreSuscripcion]=añoSuscripcion
                print(añosub)
                menu()
                opcion=int(input("Elige una opcion\n"))

    if opcion==4:
        print("")

    if opcion==5:
        print("")
    if opcion==6:
        bol=False