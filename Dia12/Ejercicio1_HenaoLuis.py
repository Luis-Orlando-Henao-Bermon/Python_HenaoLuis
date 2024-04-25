from os import system #se importa sistem para poder limpiar pantalla 
def menu(): #es una duncion que lo unico que hace es mostrar el menu
    print("-----Menu-----\n1. Crear\n2. Actualizar\n3. Revisar\n4. Eliminar\n5. Salir")

def eventosHay(): #esta es uan uncion que muestra los eventos que hay en forma vertical ademas de que le da una enumeracion
    
    for i in range(len(Eventos)):
        print(i+1,Eventos[i])
        
import json#se importa json para poder importar y exportar archivos json

with open("large-file.json", encoding="utf-8") as openFile: #se abre el archivo (large-file.son) y se le dice en que codificacion se debe leer (utf-8) posteriormente se pasa ese archivo a mijson lo cual se convierte en una lista
    mijson=json.load(openFile)

Eventos=[]# se crea una lista en donde se guardaran cada uno de los diferentes eventos que hay 
x=0
for i in range(len(mijson)):#se usa un bucle for para revisar cada una de las posiciones de mijson y cada vez que mijson en la posicion de i tenga un type(son los eventos que hay) que no este en la lista de eventos lo agregue   
    if mijson[i]["type"] not in Eventos:
        Eventos.append(mijson[i]["type"])
        x=x+1 #se usa un contador para saber cuantos eventos hay 

#se crea una lista para cada uno de los eventos que hay 
CreateEvent=[]
PushEvent=[]
WatchEvent=[]
ReleaseEvent=[]
PullRequestEvent=[]
IssuesEvent=[]
ForkEvent=[]
GollumEvent=[]
IssueCommentEvent=[]
DeleteEvent=[]
PullRequestReviewCommentEvent=[]
CommitCommentEvent=[]
MemberEvent=[]
PublicEvent=[]


#se guardaran cada uno de los eventos en la lista del tipo que le corresponde

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a CreateEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="CreateEvent":
        CreateEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a PushEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="PushEvent":
        PushEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a WatchEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="WatchEvent":
        WatchEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a ReleaseEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="ReleaseEvent":
        ReleaseEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a PullRequestEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="PullRequestEvent":
        PullRequestEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a IssuesEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="IssuesEvent":
        IssuesEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a ForkEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="ForkEvent":
        ForkEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a GollumEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="GollumEvent":
        GollumEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a IssueCommentEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="IssueCommentEvent":
        IssueCommentEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a DeleteEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="DeleteEvent":
        DeleteEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a PullRequestReviewCommentEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="PullRequestReviewCommentEvent":
        PullRequestReviewCommentEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a CommitCommentEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="CommitCommentEvent":
        CommitCommentEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a MemberEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="MemberEvent":
        MemberEvent.append(mijson[b])

for b in range(len(mijson)): #se usa un bucle que lea todo el archivo(mijson) y si el type de ese evento es igual a PublicEvent lo agrega a la lista CreateEvent
    if mijson[b]["type"]=="PublicEvent":
        PublicEvent.append(mijson[b])

#esta es una lista en donde estan todas las listas de los eventos 
eventoEnLista=[CreateEvent,PushEvent,WatchEvent,ReleaseEvent,PullRequestEvent,IssuesEvent,ForkEvent,GollumEvent,IssueCommentEvent,DeleteEvent,PullRequestReviewCommentEvent,CommitCommentEvent,MemberEvent,PublicEvent]


# se usa un try por si al pedir que se ingrese la opcion la persona ingresa una letra le pida que ingrese una opcion valida
try:
    
    menu()#se muestra el menu y le pide que ingrese la opcion 
    opcion=int(input("Ingresa una opcion\n"))

    bol1= True
    #se usa un while para que cada vez que la persona ingrese un numero diferente a los que hay en las opciones le pida que ingrese uno de los que hay alli 
    while bol1==True:

        if opcion>5 or opcion<1:
            opcion=int(input("Ingresa una opcion de las que hay en las opciones \n"))
        else:
            bol1=False

except ValueError:
    opcion=int(input("Ingresa una opcion valida (numero)\n"))

bol2=True
while bol2==True:#se usa un bucle wile para que se repita el menu cada vez que termine de ejecutar una de las opciones

    if opcion==1:#opcion de agregar
        system("clear")#se limpia pantalla
        print("-----Tipos de Eventos-----")
        eventosHay()#se muestran los eventos que hay llamando a la funcion eventosHay
        try: #se usa un try por si ingresa algo que no sea un entero, ya que la opcion que se espera es un entero 
            agregar=int(input("Que tipo de evento deseas agregar (Ingresa el numero del evento)\n"))
            bol3=True
            while bol3==True:

                if agregar>x or agregar<1:#si ingresa un numero diferentes a los que hay en los eventos le pide que  ingrese un numero de los que se ven en pantalla 
                    agregar=int(input("Ingresa un evento de los que hay en pantalla\n"))
                else:
                    bol3=False

        except ValueError:
            agregar=int(input("Ingresa una opcion valida (numero)\n"))
        
        eventoEnLista[agregar-1].append({"type":eventoEnLista[agregar-1][0]["type"]}) #Con esto se agrega el type al nuevo evento como ya se que evento es el que quiere agregar solo se lo agrego poniendo el type que hay en eventoEnLista en la pocicion agregar-1 (que es el evento que se quiere agregar uno nuevo) y dentro de alli en la pocicion 0 (la posisicon no importa mientras que este en una pocicion que haya en la lista, la pocicion no importa ya que todos los type de la lista son iguales en esa pocicion) 
        
        idAgregar=input("ingrese el nuevo id\n")#se pide el id del nuevo evento
        eventoEnLista[agregar-1][len(eventoEnLista[agregar-1])-1].update({"id":idAgregar})#se agrega el id del evento
        print("Ahora agregaremos los datos de actor")
        try:#se usa un try por si ingresa algo que no sea un entero, ya que la opcion que se espera es un entero 
            idActorAgregar=int(input("ingresa el nuevo id de actor\n"))#se pide el nuevo id de actor
        except ValueError:
            idActorAgregar=int(input("ingresa el nuevo id de actor\n"))

        loginActorAgregar=input("Ingrese el nuevo login\n")
        avatar_urlActorAgregar=input("ingrese el nuevo avatar url\n")

        eventoEnLista[agregar-1][len(eventoEnLista[agregar-1])-1].update({"actor":{"id":idActorAgregar,"login":loginActorAgregar,"avatar_url":avatar_urlActorAgregar}})#se agrega el id, login y avatar_url en el diccionario de actor que a su vez se agrega en el dicionario del evento al que se le quiere agregar 
        
        print("Ahora agregaremos los datos de repo")
        try:#se usa un try por si ingresa algo que no sea un entero, ya que la opcion que se espera es un entero 
            idRepoAgregar=int(input("ingresa el nuevo id de repo\n"))#se pide el nuevo id de repo
        except ValueError:
            idRepoAgregar=int(input("ingresa el nuevo id de repo\n"))
        nameRepoAgregar=input("Ingrese el nuevo name de repo\n")

        eventoEnLista[agregar-1][len(eventoEnLista[agregar-1])-1].update({"repo":{"id":idRepoAgregar,"name":nameRepoAgregar}})#se agrega el id, name en el diccionario de repo que a su vez se agrega en el dicionario del evento al que se le quiere agregar 

        publicAgregar=input("¿El public a agregar es true o false?\n")#Se pregunta si el public a agragar es true o false, si ingresa una opcion diferente se le pedira que la vuelva a ingresar
        if publicAgregar=="true":
            eventoEnLista[agregar-1][len(eventoEnLista[agregar-1])-1].update({"public":True})
        
        elif publicAgregar=="false":
            eventoEnLista[agregar-1][len(eventoEnLista[agregar-1])-1].update({"public":False})
        
        else:
            publicAgregarError=input("Ingresa un opcion valida true o false\n")

            if publicAgregarError=="true":
                eventoEnLista[agregar-1][len(eventoEnLista[agregar-1])-1].update({"public":True})
            
            elif publicAgregarError=="false":
                eventoEnLista[agregar-1][len(eventoEnLista[agregar-1])-1].update({"public":False})

        

        # se usa un try por si al pedir que se ingrese la opcion la persona ingresa una letra le pida que ingrese una opcion valida
        try:
            
            menu()#se muestra el menu y le pide que ingrese la opcion 
            opcion=int(input("Ingresa una opcion\n"))

            bol1= True
            #se usa un while para que cada vez que la persona ingrese un numero diferente a los que hay en las opciones le pida que ingrese uno de los que hay alli 
            while bol1==True:

                if opcion>5 or opcion<1:
                    opcion=int(input("Ingresa una opcion de las que hay en las opciones \n"))
                else:
                    bol1=False

        except ValueError:
            opcion=int(input("Ingresa una opcion valida (numero)\n"))
            
    if opcion==2:#opcion de actualizar
        system("clear")#se limpia pantalla
        print("-----Tipos de Eventos-----")
        eventosHay()#se muestran los eventos que hay llamando a la funcion eventosHay
        try: #se usa un try por si ingresa algo que no sea un entero, ya que la opcion que se espera es un entero 
            actualizar=int(input("Que tipo de evento deseas actualizar (Ingresa el numero del evento)\n"))
            bol3=True
            while bol3==True:

                if actualizar>x or actualizar<1:#si ingresa un numero diferentes a los que hay en los eventos le pide que  ingrese un numero de los que se ven en pantalla 
                    actualizar=int(input("Ingresa un evento de los que hay en pantalla\n"))
                else:
                    bol3=False

        except ValueError:
            actualizar=int(input("Ingresa una opcion valida (numero)\n"))

        for q in range(len(eventoEnLista[actualizar-1])):#se usa un bucle for para mostrar cada uno de los datos en la lista eventoEnLista en la pocicion actualizar-1 que es la pocicion del evento que desean actualizar
            print("--------------------------")
            print("------Evento",q+1,"------")
            print("--------------------------")
            print("ID:",eventoEnLista[actualizar-1][q]["id"])
        
        idActualizar=input("Que id quieres actualizar\n")#aca se lee el id que se quiere actualizar

        indiceActualizar=-1 #esto es para saber el indice del id que ingreso la persona (se pone -1 ya que es un indice que no va a estar en la lista)

        for e in range(len(eventoEnLista[actualizar-1])):#se usa un bucle for para recorrer toda la lista eventoEnlista en la pocicion actualizar-1 que es la pocicion del evento que desean actualizar

            if eventoEnLista[actualizar-1][e]["id"]==idActualizar: #si el id en eventoEnLista en la pocicion actualizar-1 y dentro de esa pocicion en la pocicion e(es la que esta recorriendo la lista ) es igual a id que se quiere acualizar,  indiceActualizar pasa a valer e(que es la pocicion en del id que es igual al que ingreso el ususario)
                indiceActualizar=e

        while indiceActualizar==-1:#si indice actualizar vale -1 significa que el id ingresado por el usuario no estaba en la lista 
            idActualizar=input("Ese id no esta, ingrese uno que si este\n")
            for e in range(len(eventoEnLista[actualizar-1])):#se usa un bucle for para recorrer toda la lista eventoEnlista en la pocicion actualizar-1 que es la pocicion del evento que desean actualizar

                if eventoEnLista[actualizar-1][e]["id"]==idActualizar: #si el id en eventoEnLista en la pocicion actualizar-1 y dentro de esa pocicion en la pocicion e(es la que esta recorriendo la lista ) es igual a id que se quiere acualizar,  indiceActualizar pasa a valer e(que es la pocicion en del id que es igual al que ingreso el ususario)
                    indiceActualizar=e
        actualizarMas="si" #actualizar mas vale "si" para que pueda empezar el bucle de while, este bucle es por si quiere actualizar mas de una cosa. ejemplo actualizar actor y repo 
        while actualizarMas=="si":#mientras actualizar mas desa igual a "si" se repetita el bucle 
            queActualizar=input("¿Que quieres actualizar?\nactor\nrepo\npublic\n")

            if queActualizar=="actor":
                try:# se usa un try por si el usuario ingresa un id con letras 
                    eventoEnLista[actualizar-1][indiceActualizar]["actor"]["id"]=int(input("Ingrese el nuevo ID\n"))
                except ValueError:
                    eventoEnLista[actualizar-1][indiceActualizar]["actor"]["id"]=int(input("Ingrese un id de solo numeros\n"))
                
                eventoEnLista[actualizar-1][indiceActualizar]["actor"]["login"]=input("Ingrese el nuevo login\n")#se pide el nuevo login y se reemplaza 
                eventoEnLista[actualizar-1][indiceActualizar]["actor"]["avatar_url"]=input("Ingrese el nuevo avatar url\n")#se pide el nuevo avatar url y se reemplaza
                actualizarMas=input("¿Quieres actualizar algo mas? si/no\n")#aca se pregunta si quiere acualizar algo mas, si la respuesta es "si" se repetita el bucle while de lo contrario se terminara el bucle y no acualizara nada mas 

            if queActualizar=="repo":

                try:# se usa un try por si el usuario ingresa un id con letras 
                    eventoEnLista[actualizar-1][indiceActualizar]["repo"]["id"]=int(input("Ingrese el nuevo ID\n"))
                except ValueError:
                    eventoEnLista[actualizar-1][indiceActualizar]["repo"]["id"]=int(input("Ingrese un id de solo numeros\n"))
                
                eventoEnLista[actualizar-1][indiceActualizar]["repo"]["name"]=input("Ingrese el nuevo name\n")

                actualizarMas=input("¿Quieres actualizar algo mas? si/no\n")#aca se pregunta si quiere acualizar algo mas, si la respuesta es "si" se repetita el bucle while de lo contrario se terminara el bucle y no acualizara nada mas

            if queActualizar=="public":

                publicAgregar=input("¿Ahora public es true o false?\n")#Se pregunta si ahora public es true o false, si ingresa una opcion diferente no se hara nada 
                if publicAgregar=="true":
                    eventoEnLista[actualizar-1][indiceActualizar]["public"]=True
                
                elif publicAgregar=="false":
                    eventoEnLista[actualizar-1][indiceActualizar]["public"]=False
                
                else:
                    print("Ingresaste una opcion invalida\n")

                actualizarMas=input("¿Quieres actualizar algo mas? si/no\n")#aca se pregunta si quiere acualizar algo mas, si la respuesta es "si" se repetita el bucle while de lo contrario se terminara el bucle y no acualizara nada mas

        # se usa un try por si al pedir que se ingrese la opcion la persona ingresa una letra le pida que ingrese una opcion valida
        try:
            
            menu()#se muestra el menu y le pide que ingrese la opcion 
            opcion=int(input("Ingresa una opcion\n"))

            bol1= True
            #se usa un while para que cada vez que la persona ingrese un numero diferente a los que hay en las opciones le pida que ingrese uno de los que hay alli 
            while bol1==True:

                if opcion>5 or opcion<1:
                    opcion=int(input("Ingresa una opcion de las que hay en las opciones \n"))
                else:
                    bol1=False

        except ValueError:
            opcion=int(input("Ingresa una opcion valida (numero)\n"))


    if opcion==3:#opcion de revisar
        system("clear")#se limpia pantalla

        print("-----Tipos de Eventos-----")
        eventosHay()#se muestran los eventos que hay llamando a la funcion eventosHay
        try: #se usa un try por si ingresa algo que no sea un entero, ya que la opcion que se espera es un entero 
            revisar=int(input("Que tipo de evento deseas revisar (Ingresa el numero del evento)\n"))
            bol3=True
            while bol3==True:

                if revisar>x or revisar<1:#si ingresa un numero diferentes a los que hay en los eventos le pide que  ingrese un numero de los que se ven en pantalla 
                    revisar=int(input("Ingresa un evento de los que hay en pantalla\n"))
                else:
                    bol3=False

        except ValueError:
            revisar=int(input("Ingresa una opcion valida (numero)\n"))

        for q in range(len(eventoEnLista[revisar-1])):#se usa un bucle for para mostrar cada uno de los datos en la lista eventoEnLista en la pocicion actualizar-1 que es la pocicion del evento que desean actualizar
            print("--------------------------")
            print("------Evento",q+1,"------")
            print("--------------------------")
            print("ID:",eventoEnLista[revisar-1][q]["id"])
            print("---Actor---")
            print("ID:",eventoEnLista[revisar-1][q]["actor"]["id"])
            print("Login:",eventoEnLista[revisar-1][q]["actor"]["login"])
            print("Avatar Url:",eventoEnLista[revisar-1][q]["actor"]["avatar_url"])
            print("---Repo---")
            print("ID:",eventoEnLista[revisar-1][q]["repo"]["id"])
            print("Name:",eventoEnLista[revisar-1][q]["repo"]["name"])
            print("--- Public:",eventoEnLista[revisar-1][q]["public"],"---")


        # se usa un try por si al pedir que se ingrese la opcion la persona ingresa una letra le pida que ingrese una opcion valida
        try:
            
            menu()#se muestra el menu y le pide que ingrese la opcion 
            opcion=int(input("Ingresa una opcion\n"))

            bol1= True
            #se usa un while para que cada vez que la persona ingrese un numero diferente a los que hay en las opciones le pida que ingrese uno de los que hay alli 
            while bol1==True:

                if opcion>5 or opcion<1:
                    opcion=int(input("Ingresa una opcion de las que hay en las opciones \n"))
                else:
                    bol1=False

        except ValueError:
            opcion=int(input("Ingresa una opcion valida (numero)\n"))
    if opcion==4:#opcion de eliminar
        system("clear")#se limpia pantalla

        print("-----Tipos de Eventos-----")
        eventosHay()#se muestran los eventos que hay llamando a la funcion eventosHay
        try: #se usa un try por si ingresa algo que no sea un entero, ya que la opcion que se espera es un entero 
            eliminar=int(input("Que tipo de evento deseas eliminar (Ingresa el numero del evento)\n"))
            bol3=True
            while bol3==True:

                if eliminar>x or eliminar<1:#si ingresa un numero diferentes a los que hay en los eventos le pide que  ingrese un numero de los que se ven en pantalla 
                    eliminar=int(input("Ingresa un evento de los que hay en pantalla\n"))
                else:
                    bol3=False

        except ValueError:
            eliminar=int(input("Ingresa una opcion valida (numero)\n"))

        for q in range(len(eventoEnLista[eliminar-1])):#se usa un bucle for para mostrar cada uno de los datos en la lista eventoEnLista en la pocicion actualizar-1 que es la pocicion del evento que desean actualizar
            print("--------------------------")
            print("------Evento",q+1,"------")
            print("--------------------------")
            print("ID:",eventoEnLista[eliminar-1][q]["id"])
            print("---Actor---")
            print("ID:",eventoEnLista[eliminar-1][q]["actor"]["id"])
            print("Login:",eventoEnLista[eliminar-1][q]["actor"]["login"])
            print("Avatar Url:",eventoEnLista[eliminar-1][q]["actor"]["avatar_url"])
            print("---Repo---")
            print("ID:",eventoEnLista[eliminar-1][q]["repo"]["id"])
            print("Name:",eventoEnLista[eliminar-1][q]["repo"]["name"])
            print("--- Public:",eventoEnLista[eliminar-1][q]["public"],"---")

        eventoEliminar=input("Ingrese el id que desea eliminar ")#se pide el id que quiere eliminar
        indexEliminar=-1 #aca se va aguardar el indice del id que sea igual al ingresado por el usuario, vale -1 ya que ese indice no se encuentra en la lista 
        while indexEliminar==-1:#mientras indexEliminar sea igual a -1 se repetira este bucle 
            for t in range(len(eventoEnLista[eliminar-1])):#se usa un bucle for para que mire en todos los puestos del type de eventoEnLista en la posicion eliminar-1(es la pocicion del evento en el que quiere eliminar)

                if eventoEnLista[eliminar-1][t]["id"]==eventoEliminar:#si algun type(que es el id) es igual al ingresado por el usuario index pasa a vale t(es la pocicion en la que esta el type igual al ingresado por el usuario)
                    indexEliminar=t

            if indexEliminar==-1:
                
                eventoEliminar=input("Ese id no esta ingrese uno de los que hay")

            del eventoEnLista[eliminar-1][indexEliminar]

        # se usa un try por si al pedir que se ingrese la opcion la persona ingresa una letra le pida que ingrese una opcion valida
        try:
            
            menu()#se muestra el menu y le pide que ingrese la opcion 
            opcion=int(input("Ingresa una opcion\n"))

            bol1= True
            #se usa un while para que cada vez que la persona ingrese un numero diferente a los que hay en las opciones le pida que ingrese uno de los que hay alli 
            while bol1==True:

                if opcion>5 or opcion<1:
                    opcion=int(input("Ingresa una opcion de las que hay en las opciones \n"))
                else:
                    bol1=False

        except ValueError:
            opcion=int(input("Ingresa una opcion valida (numero)\n"))
                
    #si escoge la opcion 5 se le agradece por usar el programa y bol2 se vuelve False terminando asi el bucle while  
    if opcion==5:
        print("Gracias por usar el programa")
        bol2=False


json_CreateEvent=json.dumps(CreateEvent)
with open("CreateEvent.json","w") as file:
    file.write(json_CreateEvent)

json_PushEvent=json.dumps(PushEvent)
with open("PushEvent.json","w") as file:
    file.write(json_PushEvent)

json_WatchEvent=json.dumps(WatchEvent)
with open("WatchEvent.json","w") as file:
    file.write(json_WatchEvent)

json_ReleaseEvent=json.dumps(ReleaseEvent)
with open("ReleaseEvent.json","w") as file:
    file.write(json_ReleaseEvent)

json_PullRequestEvent=json.dumps(PullRequestEvent)
with open("PullRequestEvent.json","w") as file:
    file.write(json_PullRequestEvent)

json_IssuesEvent=json.dumps(IssuesEvent)
with open("IssuesEvent.json","w") as file:
    file.write(json_IssuesEvent)

json_ForkEvent=json.dumps(ForkEvent)
with open("ForkEvent.json","w") as file:
    file.write(json_ForkEvent)

json_GollumEvent=json.dumps(GollumEvent)
with open("GollumEvent.json","w") as file:
    file.write(json_GollumEvent)

json_IssueCommentEvent=json.dumps(IssueCommentEvent)
with open("IssueCommentEvent.json","w") as file:
    file.write(json_IssueCommentEvent)

json_DeleteEvent=json.dumps(DeleteEvent)
with open("DeleteEvent.json","w") as file:
    file.write(json_DeleteEvent)

json_PullRequestReviewCommentEvent=json.dumps(PullRequestReviewCommentEvent)
with open("PullRequestReviewCommentEvent.json","w") as file:
    file.write(json_PullRequestReviewCommentEvent)

json_CommitCommentEvent=json.dumps(CommitCommentEvent)
with open("CommitCommentEvent.json","w") as file:
    file.write(json_CommitCommentEvent)

json_MemberEvent=json.dumps(MemberEvent)
with open("MemberEvent.json","w") as file:
    file.write(json_MemberEvent)    

json_PublicEvent=json.dumps(PublicEvent)
with open("PublicEvent.json","w") as file:
    file.write(json_PublicEvent)
#Desarrollado por Luis Henao c.c. 1093904929 