#El programa selecciona aleatoriamente un número secreto entre 1 y 100., donde el usuario tiene un total de 10 intentos 
#para adivinar el número secreto. Después de cada intento, el programa dará pistas indicando si el número secreto es 
#mayor o menor que la suposición actual del usuario. Si el usuario adivina correctamente, el programa felicitará al jugador
# y mostrará en cuántos intentos lo logró.
#El programa debe ser amigable y explicar claramente las instrucciones al usuario.

print("Jugaremos un juego\nIntentaras adivinar un numero del 1 al 100\nDespues de cada intento te estare dando pistas para que sepas\nsi el numero a adivinar es mayor o menor\nTienes 10 intentos para lograrlo\nQue comience el juego ;)")
from random import randint  #importamos randint de la libreria ramdom para hacer un numero aleatorio entre 1 y 100
a=randint(1, 100)

xd=True
x=0
while xd==True:
    x=x+1#este es un contador para lops intentos
    if x>10: #si supera los 10 intentos muestro el siguiente mensaje y termino el programa:
        print("Se acabaron tus intentos:(\nEl numero a adivinar era:", a)
        break
    intento=int(input("ingresa tu intento\n"))
    if intento<a and x<10:# si el intento es menor al numero a adivinar y lleva menos de 10 intentos muestro el siguiente mensaje:
        print("El numero a adivinar es mayor")

    if intento>a:# si el intento es menor al numero a adivinar muestro el siguiente mensaje:
        print("El numero a adivinar es menor")

    if intento==a:# si el intento es menor al numero a adivinar muestro el siguiente mensaje:
        print("Felicidades adivinaste el numero\nLo lograste en:" , x, "intentos")
        xd=False

#Desarrollado por Luis Orlando Henao Bermon c.c.1093904929