estudiante=[]
listanotas=[]
cant=int(input("Ingresa cantidad de estudiantes a registrar:_"))

for i in range (cant):
    print(f"Estudiante {i+1}")
    print("-----------------------")
    nom = input("Ingrese el nombre del estudiante:_")
    estudiante.append([nom])
    mate = input("Ingrese la materia:_")
    estudiante.append([mate])
    nota1 = float(input("Ingrese la nota 1:_ "))
    listanotas.append([nota1])
    nota2 = float(input("Ingrese la nota 2:_ "))
    listanotas.append([nota1])
    suma_ele=sum(listanotas/2)
    if suma_ele > 4:
        print(f"{nom} Gano con la nota final: {suma_ele}")
    else:
        print(f"{nom} Perdio con la nota final: {suma_ele}")
print("\nRESUMEN")
for i in range(cant):
    print(f"{estudiante[i][0]} - {estudiante[i][1]} → Nota final: {listanotas[i]}")


