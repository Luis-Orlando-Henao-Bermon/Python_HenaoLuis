#Cambio de dinero
#Problema del cambio de moneda
#Calcula el número mínimo de monedas necesarias para cambiar el valor dado en monedas de denominaciones 1, 5 y 10.
#Entrada: Dinero entero.
#Salida: El número mínimo
#de monedas con denominaciones 1, 5
#y 10 que cambia el dinero.
#¢1
#¢5 ¢10
#En este problema, implementará un sencillo algoritmo codicioso utilizado por los cajeros de todo el mundo. Suponemos que un cajero tiene un número ilimitado de monedas de cada denominación.
#Formato de entrada. Dinero entero.
#Formato de salida. El número mínimo de monedas con denominaciones 1, 5, 10 que cambia el dinero.
#Restricciones. 1 < dinero ≤ 103.
#Ejemplo 1.
#Entrada:
#2
#Output:
#2
#2=1+1.
#Muestra 2.
#Entrada:
#28
#Salida: 6
#28 10+10+5+1+1+1.

n=int(input("ingrese el numero del que quieres saber el cambio de dinero"))

def calculo(a):
    cont1=10
    num1=10
    sum1=0
    while cont1<=a:
        cont1=cont1+10
        
        print(num1)
        sum1=sum1+10
    
    num2=5
    while sum1<=a:
        sum1=sum1+5
        print(num2)
        

            
calculo(n)
