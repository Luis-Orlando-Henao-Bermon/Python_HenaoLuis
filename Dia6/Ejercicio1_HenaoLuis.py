numeros=[]
def separar(a):
    while a>0:
        b=a%10
        numeros.append(b)
        a=a//10


o=int(input())
while o<0:
    print("por favor ingrese un numero positivo")
    o=int(input())
separar(o)
x=len(numeros)

while x>300:
    
    print("Error ingresaste muchos numeros")
    o=int(input())
    numeros= []
    separar(o)
    x=len(numeros)

    
listaResuelta= []
for reps in numeros:
    if reps not in listaResuelta:
        listaResuelta.append(reps)

n= len(listaResuelta)
for i in range(n-1):
    for j in range(n-1-i):
        if listaResuelta[j]>listaResuelta[j+1]:
            listaResuelta[j], listaResuelta[j+1]= listaResuelta[j+1], listaResuelta[j]

print(listaResuelta)