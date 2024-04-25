import json# se importa json
from os import system#se importa sistem para limpiar pantalla 
with open("info.json",encoding="utf-8") as file:#se importa el archivo de info.json
    informacion=json.load(file)

def menu():#se crea una funcion para mostar el menu
    print("-----Menu-----\n1. Revisar\n2. Crear\n3. Actualizar\n4. Eliminar\n5.salir")

menu()#se meustra el menu y se pide la opcion que quieren ingresar 
opcion=int(input("ingresa una opicion de las que aparecen en pantalla\n"))
bol2=True
while bol2==True:#se usa un bucle while para poder repetir el menu infinitas veces hasta que escoga la opcion 5 que con esa opcion se acaba el bucle

    if opcion==1:
        system("clear")
        print("-----Grupos-----")

        for z in range(len(informacion)):#se muestran todos los grupos que hay  con el bucle for 
            print(z+1,informacion[z]["grupo"])

        grupoRevisar=int(input("¿Que grupo quieres revisar? (Ingrese un numero)\n"))#se pregunta que grupo desea revisar )

        for q in range(len(informacion[grupoRevisar-1]["estudiantes"])):#se usa un bucle for para mostrar todos los datos de estudiantes en el grupo informacion en la pocicion de grupoRevisar-1 que es la pocicion en la que esta el grupo 
            print("-------------------------")
            print("-------Estudiante",q+1,"-------")
            print("-------------------------")
            print("ID:",informacion[grupoRevisar-1]["estudiantes"][q]["id"])
            print("Nombre:",informacion[grupoRevisar-1]["estudiantes"][q]["nombre"])
            print("Apellido:",informacion[grupoRevisar-1]["estudiantes"][q]["apellido"])
            print("Edad:",informacion[grupoRevisar-1]["estudiantes"][q]["edad"])
            print("Fecha de nacimiento:",informacion[grupoRevisar-1]["estudiantes"][q]["fechaNacimiento"])
            print("Cedula:",informacion[grupoRevisar-1]["estudiantes"][q]["cedula"])
            print("Email:",informacion[grupoRevisar-1]["estudiantes"][q]["email"])
            print("Git Hub:",informacion[grupoRevisar-1]["estudiantes"][q]["github"])
        menu()#se meustra el menu y se pide la opcion que quieren ingresar 
        opcion=int(input("ingresa una opicion de las que aparecen en pantalla\n"))

    if opcion==2:
        system("clear")
        print("-----Grupos-----")

        for z in range(len(informacion)):#se muestran todos los grupos que hay  con el bucle for 
            print(z+1,informacion[z]["grupo"])

        grupoAgregar=int(input("¿En que grupo agregaras un estudiante?\n"))#se pide los datos del estudiante y se van agregando cada cosa en su respectivo lugar 
        
        informacion[grupoAgregar-1]["estudiantes"].append({"id":int(input("ingresa el id del estudiante\n"))})
        informacion[grupoAgregar-1]["estudiantes"][len(informacion[grupoAgregar-1]["estudiantes"])-1].update({"nombre":input("ingresa el nombre del estudiante\n")})
        informacion[grupoAgregar-1]["estudiantes"][len(informacion[grupoAgregar-1]["estudiantes"])-1].update({"apellido":input("ingresa el apellido del estudiante\n")})
        informacion[grupoAgregar-1]["estudiantes"][len(informacion[grupoAgregar-1]["estudiantes"])-1].update({"edad":int(input("ingresa la edad del estudiante\n"))})
        informacion[grupoAgregar-1]["estudiantes"][len(informacion[grupoAgregar-1]["estudiantes"])-1].update({"fechaNacimiento":input("ingresa la fecha de nacimiento del estudiante MM-DD-AAA\n")})
        informacion[grupoAgregar-1]["estudiantes"][len(informacion[grupoAgregar-1]["estudiantes"])-1].update({"cedula":int(input("ingresa la cedula del estudiante\n"))})
        informacion[grupoAgregar-1]["estudiantes"][len(informacion[grupoAgregar-1]["estudiantes"])-1].update({"email":input("ingresa el email del estudiante\n")})
        informacion[grupoAgregar-1]["estudiantes"][len(informacion[grupoAgregar-1]["estudiantes"])-1].update({"github":input("ingresa el git hub del estudiante\n")})
        
        print("Agregado con exito")

        menu()#se meustra el menu y se pide la opcion que quieren ingresar 
        opcion=int(input("ingresa una opicion de las que aparecen en pantalla\n"))


    if opcion==3:
        system("clear")
        print("-----Grupos-----")

        for z in range(len(informacion)):#se muestran todos los grupos que hay  con el bucle for 
            print(z+1,informacion[z]["grupo"])

        grupoActualizar=int(input("¿Que grupo quieres actualizar? (Ingrese un numero)\n"))#se pregunta que grupo desea Actualizar )

        for q in range(len(informacion[grupoActualizar-1]["estudiantes"])):#se usa un bucle for para mostrar todos los datos de estudiantes en el grupo informacion en la pocicion de grupoActualizar-1 que es la pocicion en la que esta el grupo 
            print("-------------------------")
            print("-------Estudiante",q+1,"-------")
            print("-------------------------")
            print("ID:",informacion[grupoActualizar-1]["estudiantes"][q]["id"])
            print("Nombre:",informacion[grupoActualizar-1]["estudiantes"][q]["nombre"])
            print("Apellido:",informacion[grupoActualizar-1]["estudiantes"][q]["apellido"])
            print("Edad:",informacion[grupoActualizar-1]["estudiantes"][q]["edad"])
            print("Fecha de nacimiento:",informacion[grupoActualizar-1]["estudiantes"][q]["fechaNacimiento"])
            print("Cedula:",informacion[grupoActualizar-1]["estudiantes"][q]["cedula"])
            print("Email:",informacion[grupoActualizar-1]["estudiantes"][q]["email"])
            print("Git Hub:",informacion[grupoActualizar-1]["estudiantes"][q]["github"])


        estudianteActualizar=int(input("¿Que estudiante deseas actualizar? (ingresa el numero del estudiante)\n"))#se pregunta el estudiante que desea actualizar para saber la picicion del estudiante y asi podere actualizar su informacion
        actualizarMas="si"#actualizarMas principalmente vale "si" porque se sabe que quiere actualizar algo
        while actualizarMas=="si":#se usa un bucle while para poder preguntarle si quiere actualizar algo mas y si  asi es se vuelva a repetir el ciclo
            queActualizar=input("¿Que deseas actualizar del estudiante\nid\nnombre\napellido\nedad\nfechaNacimiento\nemail\ngithub\n")
            #se agregan exepciones ya que es id, edad y cedula se espera un numero entero
            if queActualizar=="id":
                print("Ingrese el nuevo valor de:",queActualizar)
                idActualizar=int(input())

                informacion[grupoActualizar-1]["estudiantes"][estudianteActualizar-1]["id"]=idActualizar

            elif queActualizar=="edad":
                print("Ingrese el nuevo valor de:",queActualizar)
                edadActualizar=int(input())

                informacion[grupoActualizar-1]["estudiantes"][estudianteActualizar-1]["edad"]=edadActualizar

            elif queActualizar=="cedula":
                print("Ingrese el nuevo valor de:",queActualizar)
                edadActualizar=int(input())

                informacion[grupoActualizar-1]["estudiantes"][estudianteActualizar-1]["cedula"]=edadActualizar
        
            else:
                print("Ingrese el nuevo valor de:",queActualizar)
                datoActualizar=input()
                informacion[grupoActualizar-1]["estudiantes"][estudianteActualizar-1][queActualizar]=datoActualizar
            
            actualizarMas=input("¿Quieres actualizar algo mas? si/no\n")

        menu()#se meustra el menu y se pide la opcion que quieren ingresar 
        opcion=int(input("ingresa una opicion de las que aparecen en pantalla\n"))

    if opcion==4:
        system("clear")
        print("-----Grupos-----")

        for z in range(len(informacion)):#se muestran todos los grupos que hay  con el bucle for 
            print(z+1,informacion[z]["grupo"])

        grupoEliminar=int(input("¿De que grupo quieres eliminar un estudiante? (Ingrese un numero)\n"))#se pregunta de que grupo desea eiminar un estudiante)

        for q in range(len(informacion[grupoEliminar-1]["estudiantes"])):#se usa un bucle for para mostrar todos los datos de estudiantes en el grupo informacion en la pocicion de grupoEliminar-1 que es la pocicion en la que esta el grupo 
            print("-------------------------")
            print("-------Estudiante",q+1,"-------")
            print("-------------------------")
            print("ID:",informacion[grupoEliminar-1]["estudiantes"][q]["id"])
            print("Nombre:",informacion[grupoEliminar-1]["estudiantes"][q]["nombre"])
            print("Apellido:",informacion[grupoEliminar-1]["estudiantes"][q]["apellido"])
            print("Edad:",informacion[grupoEliminar-1]["estudiantes"][q]["edad"])
            print("Fecha de nacimiento:",informacion[grupoEliminar-1]["estudiantes"][q]["fechaNacimiento"])
            print("Cedula:",informacion[grupoEliminar-1]["estudiantes"][q]["cedula"])
            print("Email:",informacion[grupoEliminar-1]["estudiantes"][q]["email"])
            print("Git Hub:",informacion[grupoEliminar-1]["estudiantes"][q]["github"])


        estudianteEliminar=int(input("¿Que estudiante deseas eliminar? (ingresa el numero del estudiante)\n"))#se le pide el estudiante que desea eliminar con esto se sabe la pocicion del estudiante que se desea eliminar 
        del informacion[grupoEliminar-1]["estudiantes"][estudianteEliminar-1]#se usa un del ya que lo que se desea eliminar es un diccionario

        menu()#se meustra el menu y se pide la opcion que quieren ingresar 
        opcion=int(input("ingresa una opicion de las que aparecen en pantalla\n"))

    if opcion==5:
        system("clear")
        print("Gracias por usar el programa")
        bol2=False

json_informacion=json.dumps(informacion)
with open("info.json","w") as file:
    file.write(json_informacion)
#desarrollado por Luis Henao c.c.1093904929