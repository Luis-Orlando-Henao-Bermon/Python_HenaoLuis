xd={123:2400,1433:9800}
s= xd[123]+xd[1433]

cantidades={2390:12,1087:5,4365:4,1923:3,9653:33}
prod={2390:{"detroit":120000}, 1087:{"beyond to souls":50000},4365:{"assassins creed 3":40000},1923:{"call of duty black ops 2":30000},9653:{"minecraft":33000}}
print("ID----Nombre-------Precio-------Cantidades")
for clave, valor in prod.items():
    
    print(clave,valor,cantidades[clave])