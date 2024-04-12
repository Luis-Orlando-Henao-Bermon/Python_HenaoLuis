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
#Restricciones. 1 < dinero ≤ 10^3.
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



def calculo(a): #hago una funcion para que me cuente las monedas y me diga cuantas se necesitas de cada 1 y la suma de todas las monedas
    cont1=10 #este es el contador le la suma de las monedas 10 y es 10 ya que esa es la moneda mas alta 
     
    sum1=0 #esta es la suma de todas las monedas
    monedas=0 #este es el contador de la cantidad de moneda
    monedas1=0#este es el contador de la cantidad de 10
    while cont1<=a:#mientras con que es la primera moneda sea menor o igual a al numero ingresado hace lo siguiente si es mayor lo ignora y pasa al siguiente 
        cont1=cont1+10#este es el contador le la suma de las monedas 10 y es 10 ya que esa es la moneda mas alta  
        
       
        sum1=sum1+10#esta es la suma de todas las monedas
        monedas1=monedas1+1#este es el contador de la cantidad de de 10
        monedas=monedas+1#este es el contador de la cantidad total de moneda
        
    monedas2=0#este es el contador de la cantidad de 5
    
    sum2=sum1+5 #sum 2 es iguala a la suma de las monedas de 10+5 ya que queremos saber si la cantidad de monedas con una mas de 5 es menor al numero ingresado
    while sum2<=a: #mientras  sum2 sea menor al numero ingresado se hace lo siguiente 
        
        
        sum2=sum2+5 # como ya sabemos que las suma de las monedas de 10+5 es menor que el numero ingresado se le suman otros 5 para saber si con otra moneda de 5 la suma de todas las monedas es menor a el numero ingresado
        monedas2=monedas2+1#este es el contador de la cantidad de de 5
        monedas=monedas+1#este es el contador de la cantidad total de moneda

    monedas3=0#este es el contador de la cantidad de 1
    
    sum3=sum2-4 #como la suma de todas las  monedas en 5 se le suman 5 demas para saber si esa suma es menor que el numero ingresado se le resta 4 que restarle los 5 demas y sumarle 1 para saber si ese numero es mayor a el numero ingresao y todo se guarda en la variable sum3
    while sum3<=a: #si sum3 es menor al nuemro ingresado hace lo siguiente
        
        
        sum3=sum3+1  # como ya sabemos que las suma de las monedas de 10 y 5+1 es menor que el numero ingresado se le suman otro 1 para saber si con otra moneda de 1 la suma de todas las monedas es menor a el numero ingresado
        monedas3=monedas3+1#este es el contador de la cantidad de de 1
        monedas=monedas+1#este es el contador de la cantidad total de moneda
    print("Necesitas", monedas1, "monedas de $10,", monedas2, "de $5 y", monedas3, "de $1" ) # se escribe la cantidad de cada moneda 
    print("Necesitas en total", monedas, "monedas") #se escribe la cantidad de todas las monedas
        
        
n=int(input("ingrese el numero del que quieres saber el cambio de dinero\n")) #pide que ingrese el numero y si el numero es menor a 1 o mayor a 1000 que es 10^3 mande error y pida que lo vuelva a ingresar
booll=True
while booll==True:
    if n<1 or n>1000:
        n=int(input("ingrese un menor mayor a 103 y menor a 1\n"))
    else:
        booll=False
calculo(n) #se llama la funcion  que me cuenta las monedas y me diga cuantas se necesitas de cada 1 y la suma de todas las monedas

#Desarrolado por Luis Orlando Henao Bermon c.c. 1093904929
