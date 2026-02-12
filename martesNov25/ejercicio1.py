vehiculo={"NOMBRE COMÚN":["Turbo","Camion sencillo","Doble Troque","Cuatro Manos","Mini mula","Tractomula 2 troques"]
          ,"DESCRIPCION":[".","Camion de 2 ejes","Camion rigido de 3 ejes","Camion rigido de 4 ejes","Tracto camion","Tracto camion"]
          ,"PESO BRUTO VEHICULAR(TON)":[".",16,28,36,32,48]
          ,"CAPACIDAD DE CARGA(TON)":[4.5,8,17,22,15-18,30]
          ,"VOLUMEN":[18,32,36,40,65,65]}

print(vehiculo["PESO BRUTO VEHICULAR(TON)"][4])
print(vehiculo["VOLUMEN"][4])

numeros={"1":18,"2":"Angela","3":82.0,"4":1.80}
numeros.popitem()#elimina un elemento aleatoriamente
for a in numeros:
    print(a.numeros[a])
    
print(numeros.get("peso","no se encontro la key"))# mandar un mensaje
numeros_pares={"email":"sena.edu.co","ambiente":4111}
numeros.update(numeros_pares)#para agregar o actualizar