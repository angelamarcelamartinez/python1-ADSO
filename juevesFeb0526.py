portatiles = []
moviles = []

def mostrar_menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar Portátil")
        print("2. Agregar Móvil")
        print("3. Mostrar dispositivos")
        print("4. Salir")

        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Opción inválida (1 a 4)")
        except ValueError:
            print("Ingrese un número válido")

def agregar_portatil():
    portatil = {}  
    portatil["marca"] = input("Ingrese la marca del portátil: ")
    portatil["almacenamiento"] = input("Ingrese el almacenamiento del portátil: ")
    portatiles.append(portatil)
    print("Portátil guardado")

def agregar_movil():
    movil = {}  
    movil["marca"] = input("Ingrese la marca del móvil: ")
    movil["sistema_operativo"] = input("Ingrese el sistema operativo del móvil: ")
    moviles.append(movil)
    print("Móvil guardado")

def mostrar_dispositivos():
    print("\n--- PORTÁTILES ---")
    for p in portatiles:
        print(p)
    print("\n--- MÓVILES ---")
    for m in moviles:
        print(m)
while True:
    opcion = mostrar_menu()

    if opcion == 1:
        agregar_portatil()
    elif opcion == 2:
        agregar_movil()
    elif opcion == 3:
        mostrar_dispositivos()
    elif opcion == 4:
        print("Programa finalizado")
        break