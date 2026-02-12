#forma 1
datos=["arroz",1,"huevo",5,"salchicha",6]
print(datos)#para llamar a toda la lista
print(datos[4])# para llamar segun la posicion en este caso 3 y cuenta desde 0,1,2,3,4,5
print(type(datos))
datos.append("Jornada Mañana")# para agregar otro dato a la lista y luego se vuelve a imprimir 
datos.remove("huevo") # para quitar un elemento de la lista con el nombre
datos.pop(2)# elimina la posicion del elemento segun el numero 
print(len(datos))# cuenta la cantidad de datos que hay en la lista 
datos1=["SENA",2025] #se crea otra lista
datos3=datos+datos1 #se creo otra variable para sumar las dos listas y unirlas
print(datos3)# se imprime

#forma 2
list1=list(["arroz",1,"huevo",5,"salchicha",6])
print(list1)
print(list1[-3])# me primprime de derecha a izquierda empieza desde el -1 y llamaria 5
print(type(list1))
list1=list([3,4,5,6])
suma_ele=sum(list1) #para sumar elementos de una lista, tienen que ser numericos 
print(suma_ele)


