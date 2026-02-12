print("Bienvenido a estructuras de python")

print("\nMenú principal:")
print("1. Tuplas")
print("2. Listas")
print("3. Diccionario")
print("0. Salir")
opc = int(input("Escoja una opcion:_ "))

while opc != 0:
    match opc:
        case 1:
            a = ("Angela", "Marcela", "Martinez", "Ruiz")

            print("\nTUPLAS")
            print("1. Agregar elemento")
            print("2. Eliminar elemento")
            print("0. Salir")
            opc1 = int(input("Escoja una opcion:_ "))

            while opc1 != 0:

                if opc1 == 1:
                    b = list(a)
                    print("Tupla actual:", b)

                    while True:
                        elem = input("Ingrese el elemento que desea agregar:_ ")
                        b.append(elem)
                        a = tuple(b)
                        print("Tupla actualizada:", a)
                        if input("¿Desea agregar otro elemento? S/N:_ ").upper() == "N":
                            break
                elif opc1 == 2:
                    b = list(a)
                    print("Tupla actual:", b)

                    while True:
                        elem = input("Ingrese el elemento que desea eliminar:_ ")
                        if elem in b:
                            b.remove(elem)
                            a = tuple(b)
                            print("Tupla actualizada:", a)
                        else:
                            print("Elemento no encontrado")

                        if input("¿Desea eliminar otro elemento? S/N:_ ").upper() == "N":
                            break
                else:
                    print("Opción inválida")

                print("\nTUPLAS")
                print("1. Agregar elemento")
                print("2. Eliminar elemento")
                print("0. Salir")
                opc1 = int(input("Escoja una opcion:_ "))

            print("\nMenú principal:")
            print("1. Tuplas")
            print("2. Listas")
            print("3. Diccionario")
            print("0. Salir")
            opc = int(input("Escoja una opcion:_ "))
            
        case 2:
            a = ["Angela", "Marcela", "Martinez", "Ruiz"]

            print("\nLISTAS")
            print("1. Agregar elemento")
            print("2. Eliminar elemento")
            print("0. Salir")
            opc1 = int(input("Escoja una opcion:_ "))

            while opc1 != 0:

                if opc1 == 1:
                    print("Lista actual:", a)
                    while True:
                        elem = input("Ingrese elemento:_ ")
                        a.append(elem)
                        print("Lista actualizada:", a)
                        if input("¿Desea agregar otro elemento? S/N:_ ").upper() == "N":
                            break


                elif opc1 == 2:
                    print("Lista actual:", a)
                    while True:
                        elem = input("Ingrese elemento a eliminar:_ ")
                        if elem in a:
                            a.remove(elem)
                            print("Lista actualizada:", a)
                        else:
                            print("Elemento no encontrado")

                        if input("¿Desea eliminar otro elemento? S/N:_ ").upper() == "N":
                            break


                else:
                    print("Opción inválida")

                print("\nLISTAS")
                print("1. Agregar elemento")
                print("2. Eliminar elemento")
                print("0. Salir")
                opc1 = int(input("Escoja una opcion:_ "))

            print("\nMenú principal:")
            print("1. Tuplas")
            print("2. Listas")
            print("3. Diccionario")
            print("0. Salir")
            opc = int(input("Escoja una opcion:_ "))
            
        case 3:
            a = {"documento": 1107975116, "nom": "Angela", "edad": 21}
            print("\nDICCIONARIO:")
            print(a)

            # Regresar al menú principal
            print("\nMenú principal:")
            print("1. Tuplas")
            print("2. Listas")
            print("3. Diccionario")
            print("0. Salir")
            opc = int(input("Escoja una opcion:_ "))
            
        case _:
            print("Opción incorrecta")

            print("\nMenú principal:")
            print("1. Tuplas")
            print("2. Listas")
            print("3. Diccionario")
            print("0. Salir")
            opc = int(input("Escoja una opcion:_ "))

print("Programa finalizado")
