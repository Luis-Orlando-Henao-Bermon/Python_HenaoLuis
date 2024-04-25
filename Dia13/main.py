#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

def abrirArchivo():
    miJSON=[]
    with open('info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("info.json","w") as outfile:
        json.dump(miData,outfile)


print("################")
print("## PLATAFORMA DE GESTION ##")
print("################")
print("")
print("Hola! Por favor escoge alguna de las opciones:\n1.Revisar estudiantes\n2.Modificar estudiante")
x=int(input("Cual opción escoges:"))
miInfo=[]
if(x==1):
    miInfo=abrirArchivo()
    for i in miInfo[0]["estudiantes"]:
        print("################")
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
elif(x==2):
    miInfo=abrirArchivo()
    contador = 0
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador = 0
    estudiante = int(input("Cual numero de identificacion vas a cambiar?"))
    datoCambiar=int(input("Que te gustaría cambiar del estudiante:\n1.Apellido:"))
    if (datoCambiar==1):
        nuevoApellido = input("Ingresa el nuevo apellido:")
        miInfo[0]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador = 0

