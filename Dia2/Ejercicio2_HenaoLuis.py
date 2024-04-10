#Este programa simula un juego interactivo en el que el usuario debe adivinar un número secreto elegido aleatoriamente
#por el programa. El número secreto está en el rango de 1 a 100. Después de cada intento del usuario, el programa proporciona
#pistas indicando si el número secreto es mayor o menor que la suposición actual. El objetivo es adivinar el número secreto en 
#la menor cantidad de intentos posible.
print("Jugaremos un juego\nIntentaras adivinar un numero del 1 al 100\nDespues de cada intento te estare dando pistas para que sepas\nsi el numero a adivinar es mayor o menor\nLa idea es que lo hagas en la menor cantidad de intentos\nQue comience el juego ;)")
from random import randint #importamos randint de la libreria ramdom para hacer un numero aleatorio entre 1 y 100
a=randint(1, 100)

xd=True
x=0
while xd==True:
    x=x+1 # este es un contador para los intentos 
    intento=int(input("ingresa tu intento\n")) #pedimos que ingrese el intento 
    if intento<a: # si el intento es menor al numero a adivinar muestro el siguiente mensaje:
        print("El numero a adivinar es mayor")

    if intento>a:# si el intento es mayor al numero a adivinar muestro el siguiente mensaje:
        print("El numero a adivinar es menor")

    if intento==a:# si el intento es igual al numero a adivinar muestro el siguiente mensaje:
        print("Felicidades adivinaste el numero\nLo adivinaste en:" , x, "intentos")
        xd=False
    
    
#Desarrollado por Luis Orlando Henao Bermon c.c.1093904929