from os import system

def articulos():# funcion para mostrar los articulos que hay en inventario
    print("Articulo-------Precio-------Cantidad")
    print("1. mancuernas ajustables - $50 - 15\n2. barra olimpica - $150 - 30\n3. banco de pesas - $100 35\n4. maquina de cardio - $800 - 10\n5. bandas de resistencia - $20 - 50")

def menu():# funcion para mostrar el menu de opciones
    print("1. ver articulos\n2. Añadir al carrito\n3. Mostrar carrito\n4. Salir del programa")

inventario=[["mancuernas ajustables",50,15],["barra olimpica",150,30], ["banco de pesas",100,35], ["maquina de cardio",800,10,], ["bandas de resistencia",20,50]] #lista en donde esta el inventario
carrito=[]

menu()#se muestra el menu de opciones
opcion=int(input("Elige una opcion\n"))
while opcion<1 or opcion>4:# si la opcion ingresado por el usuario es mayor a 4 o menor que uno significa que no es una opcion valida y le pide que la vuelva a ingresar
    opcion=int(input("Ingrese una opcion valida\n")) #switch case ?

posicion=0 #este es un contador para saber la pocicion en la que se esta en el carrito se usa en la opcion 2

bol=True
while bol==True: #mientras bol sea verdadero se ejecutara el programa en bucle 
    if opcion==1:

        system("cls") #esto es para limpiar pantalla 

        print("Articulo-------------Precio-------Cantidad")
        for i in range(len(inventario)): #se usa un bucle for para mostrar cada uno de los aticulos que estan separados por listas en la lista inventario 
            print(i+1,inventario[i])

        menu()#se muestra el menu de opciones
        opcion=int(input("Elige una opcion\n"))
        while opcion<1 or opcion>4:# si la opcion ingresado por el usuario es mayor a 4 o menor que uno significa que no es una opcion valida y le pide que la vuelva a ingresar
            opcion=int(input("Ingrese una opcion valida\n"))

    if opcion==2:
        system("cls") #esto es ppara limpiar pantalla 

        print("Articulo-------------Precio-------Cantidad")
        for i in range(len(inventario)): #se usa un bucle for para mostrar cada uno de los aticulos que estan separados por listas en la lista inventario 
            print(i+1,inventario[i])

        #se pregunta el ariculo que quiere y si el nuemro que ingresa es no esta en los que hay en pantalla le pida que ingrese uno valido
        articuloAgregar=int(input("¿Que articulo deseas agregar al carrito? Ingresa su numero\n"))

        while articuloAgregar>len(inventario) or articuloAgregar<1:
            articuloAgregar=int(input("Ingresa un ariculo valido\n"))
        #en una nueva lista llamada carrito se agrega la lista que hay en la pocicion del producto que desea (las listas estan en otra lista llamada inventario)
        
        carrito.append(list(inventario[articuloAgregar-1]))#aca se agrega a la lista de carrito las lista que haya en el inventario en la posicion de el articulo que haya ingresado menos 1 ya que las listas empiezan en la posicion 0, para que agregue la lista como aparte y no la clone se usa el list
        
        posicion+=1#este es un contador para saber en que posicion del carrito se esta y se pueda poner la cantidad a llevar 
        
        #se pregunta la cantidad a llevar y si la cantidad a llevar es mayor a la que hay en inventario le pide que ingrese una menor 
        cantidadAgregar=int(input("¿Que cantidad deseas llevar?\n"))
        while cantidadAgregar>inventario[articuloAgregar-1][2]:
            print("No tenemos esa cantidad por favor ingresa una cantidad menor")
            cantidadAgregar=int(input())
        
        carrito[posicion-1][2]=cantidadAgregar#se pone la cantidad en el carrito como la cantidad que desea llevar
        
        inventario[articuloAgregar-1][2]=inventario[articuloAgregar-1][2]-cantidadAgregar #aca se le resta la cantidad añadida al carrito a la cantidad del inventario
        
        menu()#se muestra el menu de opciones
        opcion=int(input("Elige una opcion\n"))
        while opcion<1 or opcion>4:# si la opcion ingresado por el usuario es mayor a 4 o menor que uno significa que no es una opcion valida y le pide que la vuelva a ingresar
            opcion=int(input("Ingrese una opcion valida\n"))
        

    if opcion==3:
        
        if len(carrito)>=1:

            print("Articulo-------------Precio-------Cantidad")
            for x in range(len(carrito)):# se usa un bucle for para mostrar las lista que hay en la lista carrito 
                print(x+1,carrito[x])

        else:
            print("No has comprado nada")

        menu()#se muestra el menu de opciones
        opcion=int(input("Elige una opcion\n"))
        while opcion<1 or opcion>4:# si la opcion ingresado por el usuario es mayor a 4 o menor que uno significa que no es una opcion valida y le pide que la vuelva a ingresar
            opcion=int(input("Ingrese una opcion valida\n"))

    if opcion==4:#si escoge la opcion 4 bol se volvera falso y se acabara el programa
        print("Gracias por usar el programa :)")
        bol=False

#Desarrollado por Luis Orlando Henao Bermon c.c. 10939049229 