palabra="De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2025"
posicion1=palabra.find("@u") #para buscar letras o palabras 
print(posicion1)
posicion2=palabra.find(" S",posicion1)
print(posicion2)
posicion3=palabra[posicion1:posicion2]
print(posicion3)

posicion1=palabra.find("J") #para buscar letras o palabras 
print(posicion1)
posicion2=palabra.find("16",posicion1)
print(posicion2)
posicion3=palabra[posicion1:posicion2]
print(posicion3)