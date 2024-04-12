#1. Crear una función que determina si un número dado por el usuario es primo. Un número primo es aquel que solo es divisible por 1 y por sí mismo. El programa proporciona un 
#menú interactivo que permite al usuario ingresar números para ser verificados como primos. Además, se incluye la opción de detener el proceso cuando el usuario lo desee.


#Al inicio, el programa dará la bienvenida y explicará el propósito del aplicativo: verificar si un número dado es primo o no.
#Se presentará un menú con opciones numeradas para que el usuario pueda elegir entre verificar un número, detener el programa u obtener información adicional.
#Si elige verificar un número, se le solicitará ingresar el número deseado.
#La función verificará si el número es primo y proporcionará un mensaje claro indicando el resultado.
#Después de cada verificación, se volverá al menú para permitir al usuario realizar más acciones.
#Si elige detener el programa, se le despedirá y el programa se cerrará.
#Si elige obtener información adicional debe arrojar una explicación de los números primos y el nombre del autor del aplicativo.


from os import system
def numeroPrimo(a): #hago una funcion para que divida el numero ingresado en todas las diviciones desde el 1 hasta ese numero y cada vez que el residuo sea 0 sume 1 al contador
    x=0
    for i in range(1, a+1): #se empieza desde 1 porque si se empezara desde 0 se dividira por cero y esa operacion da infinito por lo tanto empieza por 1 y hasta el numero ingresado +1 ya que pues si empieza desde 1 hay que sumarle 1 para que haga todos los numeros
        if a%i==0:
            x=x+1
        
    if x==2: #si solo hay 2 en el contador el numero es primo de lo contrario no lo es
        print("El numero ingresado es primo")
    else:
        print("El numero ingresado no es primo")

def menu(): #Esta es una funcion para que me escriba el menu
    print("Bienvenido\nMenu de opciones\n1. Verificar numero\n2. Detener el programa\n3. Obtener mas informacion\nEscoge una opcion")

menu()
Opcion=int(input()) #se escribe el menu y se lee la opcion
booll=True
while booll==True: #mientras booll sea verdadero se ejecutara el programa 
    while Opcion>3 or Opcion<1: #ya que en el menu solo hay 3 opciones si la opcion es mayor que 3 y menor que uno le mande un mensaeje
        Opcion=int(input("Por favor Escribe una opcion valida\n"))

    if Opcion==1:
        
        n=int(input("Ingresa el numero que quieres saber si es primo\n")) #si escoge la opcion 1 pregunta el numero y mira si es primo en la funcion numeroPrimo
        numeroPrimo(n)
        menu() #se vuelve a escribir el menu y lee la opcion 
        Opcion=int(input())
    
    if Opcion==2:
        print("Gracias por usar el programa") #si escoge la opcion 2 le dara las gracias por usar el programa y se cerrara el programa
        booll=False

    if Opcion==3: #si escoge la opcion 3 dira que es un numero primo y el autor del aplicativo
        print("Un número primo es aquel que solo es divisible por 1 y por sí mismo\nLuis Henao c.c. 1093904929")
        menu()
        Opcion=int(input()) #se vuelve a escribir el menu y lee la opcion 

#Desarrolado por Luis Orlando Henao Bermon c.c. 1093904929
    