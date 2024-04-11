#1. Crear una función que determina si un número dado por el usuario es primo. Un número primo es aquel que solo es divisible por 1 y por sí mismo. El programa proporciona un 
#menú interactivo que permite al usuario ingresar números para ser verificados como primos. Además, se incluye la opción de detener el proceso cuando el usuario lo desee.


#Al inicio, el programa dará la bienvenida y explicará el propósito del aplicativo: verificar si un número dado es primo o no.
#Se presentará un menú con opciones numeradas para que el usuario pueda elegir entre verificar un número, detener el programa u obtener información adicional.
#Si elige verificar un número, se le solicitará ingresar el número deseado.
#La función verificará si el número es primo y proporcionará un mensaje claro indicando el resultado.
#Después de cada verificación, se volverá al menú para permitir al usuario realizar más acciones.
#Si elige detener el programa, se le despedirá y el programa se cerrará.
#Si elige obtener información adicional debe arrojar una explicación de los números primos y el nombre del autor del aplicativo.


#2. Implementar un generador de contraseñas seguras que permite al usuario especificar la longitud de la contraseña y decidir si desea incluir mayúsculas, minúsculas, 
#caracteres alfanuméricos y símbolos. La generación de contraseñas se realiza a través de una función que toma la longitud y las preferencias del usuario y devuelve una 
#contraseña segura. El programa ofrece un menú interactivo para probar el generador de contraseñas y permite al usuario realizar múltiples solicitudes.


#Al inicio, el programa dará la bienvenida y proporcionará una descripción del generador de contraseñas seguras.
#Presentará un menú con opciones numeradas para que el usuario pueda elegir la longitud de la contraseña, incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos.
#Utilizará una función para generar la contraseña según las preferencias del usuario.
#Mostrará la contraseña generada y preguntará si el usuario desea generar otra contraseña.
#Si el usuario decide salir, se despedirá y el programa se cerrará.
#Se manejarán casos de entrada no válida, como letras en lugar de números para la longitud de la contraseña.

def numeroPrimo(n):
    if n%2==0:
        print("El numero ingresado es primo")
    else:
        print("El numero ingresado no es primo")

def menu():
    print("Menu de opciones\n1. Verificar numero\n2. Detener el programa\n3. Obtener mas informacion\nEscoge una opcion\n")

menu
n=input()

if n>3 and n<1:
    n=int(input("Por favor Escribe una opcion valida"))



