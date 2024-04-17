from os import system#se importa system de la libreria os para limpiar pantallla

def menuOpcion(): #esta es una funcion para que muestre el menu de opciones 

    print("\nMENU DE OPCIONES")
    print("1. Agregar productos al carrito")
    print("2. Ver el contenido del carrito ")
    print("3. Calcular el total de la compra")
    print("4. Finalizar la compra ")

precios={2390:120000,1087:50000,4365:40000,1923:30000,9653:33000}#este diccionario contiene el ID y su precio
cantidades={2390:12,1087:5,4365:4,1923:3,9653:33}#este diccionario contiene e ID y la cantidad del producto

print("")
print("A GAMES PLACE \n ")
print("¡Bienvenido al paraíso de los juegos!\nPrepárate para sumergirte en un mundo de diversión, emoción y aventuras virtuales.\nEstamos emocionados de tenerte aquí y ayudarte a encontrar los mejores juegos para que disfrutes al máximo.\n Let's play!\n ")

#se muestran los juegos que hay en el catalogo
prod={2390:{"detroit":120000}, 1087:{"beyond to souls":50000},4365:{"assassins creed 3":40000},1923:{"call of duty black ops 2":30000},9653:{"minecraft":33000}}

print("ID----Nombre-------Precio-----Cantidad")
for clave, valor in prod.items():#con esto se muestra lo que esta en el diccionario de productos (prod) y tambien las cantidades en vertical 
    
    print(clave,valor,cantidades[clave])

#se llama la funcion menuOpcion para mostrar el menu de opciones  
menuOpcion()

opcion=int(input())
recivo={} #este es un diccionario vacio para los productos que agrega el usuario al carrito
cantidadRecivo={} #este es un diccionario vacio que agrega las cantidades que quiere el usuario de cada procucto al carrito

contador=0 #este es el contador que usamos para sumar los productos por las cantidades agregadas al carrito

bol=True
while bol==True:
    if opcion==1:
        system("cls")#esto es para limpiar pantalla
        print("ID----Nombre-------Precio----Cantidad")
        
        for clave, valor in prod.items():#con esto se muestra lo que esta en el diccionario de productos (prod) y tambien las cantidades en vertical
            print(clave,valor,cantidades[clave])

        pAgregar=int(input("¿Que producto deseas agregar? Por favor usa el ID único\n"))
        
        if pAgregar in prod:# si el id ingresado esta en el diccionario de prod lo agrega al recivo de lo contrario le rechaza el intento de añadir al carritoy le muestra el menu principal
            recivo[pAgregar]= prod[pAgregar]
            bol2=True
            
            while bol2==True: #este while se usa por si la cantidad que quiere llevar es mayor a la que hay en el inventario le mande error y le permita que lo vuelva a intentar 
                
                cAgregar=int(input("¿Que cantidad deseas llevar?\n"))
                
                if cAgregar<=cantidades[pAgregar]:#si la cantidad que quiere llevar es menor o igua a la cantidad en inventario busca la cantidad que hay en inventario y le resta la cantidad que quiere llevar y termina el ciclo while
                    cantidades[pAgregar]=cantidades[pAgregar] -cAgregar
                
                    bol2=False
                
                else:
                
                    print("No tenemos la cantidad de productos que quieres en el inventario :( \nVuelve a intentarlo")
            
            cantidadRecivo[pAgregar]=cAgregar #esto agrega al diccionario de cantidadRecivo en el id del producto que quiere llevar la cantidad que desea llevar
            contador=contador+precios[pAgregar]*cAgregar #en este contador se van sumando los productos por la cantidad para ir llevando el total de la compra 
            
            
            print("Su compra ha sido agregada con exito")
        
        else:
        
            print("Este producto no esta en el inventario\nIntento de agregar al carrito rechazado :(") 
        print("-----------------------------------------------------------------------")
        print("PRODUCTOS COMPRADOS") #cada vez que se agregue un producto se va mostrando un recivo que muestra el producto, la cantidad y el total de las cosas agregadas al carrito
        print("ID----Nombre-------Precio----Cantidad")
        for a,b in recivo.items():#con esto se muestra lo que esta en el diccionario de recivo y tambien las cantidades en vertical (estas son las cosas agregadas al carrito)
            print(a,b,cantidadRecivo[a])
        
        print("El total de su compra es: ",contador) #esto muestra la cantidad de los productos agregados al carrito
        menuOpcion() #se vuelve a mostrar el menu y se lee la opcion a escoger
        
        opcion=int(input()) 

    if opcion==2:
        
        system("cls") #con esto limpia pantalla
        
        print("ID----Nombre-------Precio----Cantidad")
        for a,b in recivo.items():#con esto se muestra lo que esta en el diccionario de recivo y tambien las cantidades en vertical (estas son las cosas agregadas al carrito)
            print(a,b,cantidadRecivo[a])
        
        menuOpcion()#se vuelve a mostrar el menu y se lee la opcion a escoger
        
        opcion=int(input())

    if opcion==3:

        system("cls")#con esto limpia pantalla
        
        print("El total de su compra es: ",contador)#esto muestra la cantidad de los productos agregados al carrito
        
        menuOpcion()#se vuelve a mostrar el menu y se lee la opcion a escoger
        
        opcion=int(input())
    
    if opcion==4:
        
        system("cls")#con esto limpia pantalla
        
        #se muestran los productos en el carrito con el total y se agradece por usar nuestra tienda y finaliza el programa 
        print("PRODUCTOS COMPRADOS ")
        print("ID----Nombre-------Precio----Cantidad")
        for a,b in recivo.items():
            print(a,b,cantidadRecivo[a])
        
        print("El total de su compra es: ",contador)
        print("\n¡Gracias por usar nuestra tienda de videojuegos")
        print("Hasta la proxima! :)")
        
        bol=False

#Desarrollado por luis Henao c.c.1093904929 y Valerie lasso T.I.1093296678