# Al inicio, el programa dará la bienvenida y explicará la naturaleza de la Secuencia de Fibonacci, donde solicitará
# al usuario ingresar un valor entero "n", representando hasta qué término de la secuencia se generará. Aquí mostrará la
# secuencia de Fibonacci hasta el enésimo término ingresado por el usuario. Luego, preguntará si el usuario desea continuar
# o salir, donde si se decide salir, el programa se detendrá; de lo contrario, se repetirá el proceso.

print ("Bienbenido te explicare la naturaleza de la secuencia de Fibonacci\nEn matemática, la sucesión de Fibonacci se trata de una serie infinita de números naturales que empieza con un 0 y un 1 y continúa añadiendo números que son la suma de los dos anteriores")

xd=True
while xd==True:
    num=int(input("Ingresa un numero y te mostrare la secuecia hasta ese valor\n"))

    a=0 #primero asignamos los valores de los primeros 2 numeros 
    b=1
    num=num-2 #se le resta 2 a num ya que  el ciclo empieza desde el tercer valor de la secuencia Fibonacci lo que significa que hay 2 mas atras y por eso se le resta 2
    print(a) #mostramos los primeros 2 valores de la secuencia 
    print(b)
    for i in range(0, num):#el ciclo se hace desde el puesto 0 hasta el puesto num que es el ingresado por el usuario y ya se le restaron 2
        
        c=b+a #hacemos la suma de a + b
        if c<99999999999 : #si la secuencia supera los 11 terminos se acaba la secuencia (asi me lo explicaron)
            print (c) #se escribe la suma 
            a=b #se reemplaza a por b que es el numero anterior al resultado de la suma que es el nuevo valor de la secuencia
            b=c #se reemplaza b por c que es la suma de los 2 numeros anteriores
            
        else:
            print("El siguiente numero supera los  11 terminos") #si la secuencia supuera los 11 terminos le escribo el sigiente mensaje y termino la secuencia 
            break
            
    
    h=input("Quieres ingresar otro numero si/no\n")#pregunto si quiere ingresar otro numero y si la respuesta es "no" se acaba el programa
    if h=="no":
        xd=False

#Desarrollado por Luis Orlando Henao Bermon c.c.1093904929