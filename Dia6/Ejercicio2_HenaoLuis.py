
#!!Al ejecutar el codigo¡¡ en la primera linea se escriben los numeros de la lista separados por espacios y en la segunda linea se escribe el numero que se quiere saber con la suma de cuales se da ese numero

datos_crudos = input()#primero se introducen los numeros de la lista y se leen en str
lista_datos = [int(d) for d in datos_crudos.split()] # se pasan los datos de datos_crudos de str a int y se guarda en lista_datos
numsuma=int(input()) #esto es para leer el nummero objetivo que es al sumar dos de la lista
posicion1= []#se crean listas vacias para guardar todas las opciones posibles que logren el objetivo
posicion2=[]
for i in range(len(lista_datos)): #se usan 2 bucles for para que por cada numero haga la suma con todos los numeros de la lista
    for a in range(len(lista_datos)):
        if lista_datos[i]+ lista_datos[a]==numsuma: #se mira si el numero i (tomemos como ejemplo la pocicion 0) al sumarse con cada numero de la lista da como resultado el objetivo
            posicion1.append(i) #si la suma de esos numeros da el objetivo se va guardando en en las lista posicion 1 y posicion 2
            posicion2.append(a)
            
            break
    
print("[",posicion1[0],",", posicion2[0],"]") #muestras las pociciones de la primera opcion para llegar al objetivo 
#desarrollado por Luis Orlando Henao Bermon c.c.1093904929