#-----------------------------------------
#-----Dia1 Cheat Sheet Python-------------
#-----------------------------------------
#Datos primitivos

#Numero
numerito=int
numerito = 1 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))

#Decimal
numeritoDecimal=float
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
miBooleanito=bool
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto=str
texto = "MI TIBU"
print(texto)
print(type(texto))





#Ingresa por teclado la infomarcion
print("Ingresa tu informacion")
nombre=input()

#Conversion de tipos de variable
numerito=float
numerito = 1.2 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))

numeritoDecimal=int
numeritoDecimal = 2
print(numeritoDecimal)
print(type(numeritoDecimal))

miBooleanito=str
miBooleanito = "True"
print(miBooleanito)
print(type(miBooleanito))

texto=bool
texto = False
print(texto)
print(type(texto))

#Bucles For y While

#bucle while

xd=1

while xd<=10:
    print(xd)
    xd=xd+1


#bucle for
colores=["amarillo", "blanco", "negro", "rojo"]
for a in colores:
    print(a)


#Funciones (4 Tipos)
#sin parametros y sin retornos

def funcion1():
    print("mi nombre es luis")

funcion1()
#con parametros y sin retorno
def funcion2(c):
    print (c + " XD")

funcion2("holaaa")
#si parametros y con retorno
def funcion3():
    resul=4*5
    return resul

resul = funcion3()
print (resul)

#con parametros y con retorno

def funcion3(x, y):
    resul=x*y
    return resul

resul = funcion3(6, 9)
print (resul)


#Desarrollado por luis Henao c.c.: 1093904929