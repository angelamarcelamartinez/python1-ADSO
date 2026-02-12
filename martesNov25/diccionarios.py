mis_datos={"nomnre":"Cesar","Apellidos":"esquivel","edad":"30","caracteristicas":("jean","reloj")
           ,"nombre":"pepito","Aprendices":["pacho",12,"milena",19]}
   #toma el ultimo valor para reescribir una key 
print(len(mis_datos)) #cantidad
print(mis_datos["Apellidos"])#para acceder por medio de la key
mis_datos["edad"]=45 #Cambierle el valor a una key 
mis_datos["zapatos"]="tennis"#añadir otra key 
print(mis_datos.get("caracteristicas"))#para llamar por medio del metodo get 
print(mis_datos["Apellidos"][0])#para llamar a una posicion de una tupla

companeros={"1":["Samuel Giron",18,"samuelgirong2007@gmail.com"],"2":["Jose Lopez",20,
        "joselopezpava0403@gmail.com"],"3":["Julian Prado",21,"julianprado0812@gmail.com"],
        "4":["Kevin Prado",17,"pradak512@gmail.com"]}

print(companeros["1"][0])
print(companeros["2"][0])
print(companeros["3"][0])
print(companeros["4"][0])

factura={"item":["Lapiz","Carpeta","Marcador"],"cantidad":[3,10,5],"valor":[3.50,4.25,7.86]}
print(factura)
factura["item"].append("Borrador")
print(factura["item"])
factura["cantidad"].append("15")
factura["valor"].append("10.55")

