#2. Implementar un generador de contraseñas seguras que permite al usuario especificar la longitud de la contraseña
# y decidir si desea incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos. La generación de contraseñas 
#se realiza a través de una función que toma la longitud y las preferencias del usuario y devuelve una contraseña segura. 
#El programa ofrece un menú interactivo para probar el generador de contraseñas y permite al usuario realizar múltiples solicitudes.


#Al inicio, el programa dará la bienvenida y proporcionará una descripción del generador de contraseñas seguras.
#Presentará un menú con opciones numeradas para que el usuario pueda elegir la longitud de la contraseña, incluir mayúsculas, 
#minúsculas, caracteres alfanuméricos y símbolos.
#Utilizará una función para generar la contraseña según las preferencias del usuario.
#Mostrará la contraseña generada y preguntará si el usuario desea generar otra contraseña.
#Si el usuario decide salir, se despedirá y el programa se cerrará.
#Se manejarán casos de entrada no válida, como letras en lugar de números para la longitud de la contraseña.

import random #se importa la libreria de ramdom ya que de alli necesito "sample"

def menu1(): #esta es una funcion para el menu
    print("Bienvenido\nEste es un generador de contraseñas en base a tus condiciones y la longitud que quieras de la contraseña se creara una contraseña para ti\nMenu\n1. longitud de la contraseña\n2. Condiciones de la contraseña\n3. Ver contraseña\n4. Salir del programa ")

def contraseña(a,b,c,d):# esta es una funcion para generar las contraseñas
    try: # este try es por si no ingresaron la longitud se lop diga al usuario
        if a=="si": #este es el primer parametro y en caso de que el parametro sea "si" le de las letras en mayuscula a la variable may y en caso contrario no le de ninguna letra
            may="QWERTYUIOPASDFGHJKLZXCVBNM"
        else:
            may=""

        if b=="si": #este es el segundo parametro y en caso de que el parametro sea "si" le de las letras en minuscula a la variable minu y en caso contrario no le de ninguna letra
            minu=("qwertyuiopasdfghjklzxcvbnm")

        else:
            minu=""
        if c=="si":#este es el tercer parametro y en caso de que el parametro sea "si" le de los numeros a la variable num y en caso contrario no le de ningun numero
            num="0123456789"
        else:
            num=""

        if d=="si":#este es el cuarto parametro y en caso de que el parametro sea "si" le de las letras en mayuscula a la variable sim y en caso contrario no le de ningun simbolo
            sim=",.-;:_{}[]()+/*!$#%&/="
        else:
            sim=""

        base=may+minu+num+sim #aca se ponen todas las variables de los parametros unidas en una sola variable
        contra=random.sample(base, longitud) #se usa sample para que escoja aleatoriamente estre todo lo que haya en la variable base y se escoje la natidad de caracteres en base a la longitud ingresada
        password="".join(contra) #esto lo que hace es que en las "" guarde todos los caracteres escogidos y los una
        print(password)
    except (NameError,): #si la persona no da una longitud le mustra lo siguiente 
        print("Tienes que poner una longitud")

    
    
menu1() # se muestra el menu y se lee la opcion
Opcion1=int(input())
booll=True
while booll==True: #mientras boll sea verdadero se repetira el programa  
    while Opcion1>4 or Opcion1<1: #ya que en el menu solo hay 4 opciones si la opcion es mayor que 4 y menor que uno le mande un mensaeje
        Opcion1=int(input("Por favor Escribe una opcion valida\n"))

    
    if Opcion1==1: #si escoge la opcion 1 le pedira la longitud y se cleve a mostrar el menu y se lee la opcion y en caso de que de una letra en vez de un numero le manda error 
        
        try:
            longitud=int(input("Ingrese la longituda de la contraseña\n"))
            menu1()
            Opcion1=int(input())
            while Opcion1>4 or Opcion1<1:#ya que en el menu solo hay 4 opciones si la opcion es mayor que 4 y menor que uno le mande un mensaeje
                Opcion1=int(input("Por favor Escribe una opcion valida\n"))
        except ValueError:
            print("Por favor ingrese un numero entero\n")

    if Opcion1==2: # se pregunta que condiciones le quiere poner a la contraseña
        print("Debes escoger por lo menos una condicion para la contraseña") #debes decir "si" a por lo menos una condicion de lo contrario te lo dira al momento de querer ver la contraseña
        mayusculas=input("¿Quieres añadir mayusculas si/no?")
        minusculas=input("¿Quieres añadir minusculas si/no?")
        numeros=input("¿Quieres añadoir caracteres alfanumericos si/no?")
        simbolos=input("¿Quieres añadir simbolos si/no")
        menu1() #se vuelve a mostrar el menu y leer la opcion
        Opcion1=int(input())
        while Opcion1>4 or Opcion1<1:#ya que en el menu solo hay 4 opciones si la opcion es mayor que 4 y menor que uno le mande un mensaeje
            Opcion1=int(input("Por favor Escribe una opcion valida\n"))


    if Opcion1==3:
        try:
            
            contraseña(mayusculas, minusculas, numeros, simbolos) #se aplica la funcion contraseña y con las variables el en el orden que se ve
        except NameError: #aca es donde se ve si ingreso o no una condicion si no se ingreso nada se mostrara este mensaje 
            print("Por favor diga que si a por lo menos una condicion de la contraseña")
        
        menu1() #se vuelve a mostrar el menu y leer la opcion
        Opcion1=int(input())
        while Opcion1>4 or Opcion1<1:#ya que en el menu solo hay 4 opciones si la opcion es mayor que 4 y menor que uno le mande un mensaeje
            Opcion1=int(input("Por favor Escribe una opcion valida\n"))
    if Opcion1==4: #se da las gacias por usar el programa y setermina el programa 
        print("Gracias por usar el programa")
        booll=False
#Desarrolado por Luis Orlando Henao Bermon c.c. 1093904929