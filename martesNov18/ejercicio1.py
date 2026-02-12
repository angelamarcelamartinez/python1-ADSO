opc = input("¿Desea salir del programa? (S para salir): ")
while opc.upper() != "S":
    cant = int(input("Ingresa cantidad de estudiantes a registrar (mínimo 4): "))
    while cant < 4:
        print("Debe ingresar mínimo 4 estudiantes.")
        cant = int(input("Ingresa cantidad de estudiantes a registrar (mínimo 4): "))
        i=0
        listnom = []
        listesta = []
        listedad = []
    for i in range(cant):
        print(f"\nEstudiante {i + 1}")
        nom = input("Ingrese el nombre del estudiante: ")
        listnom.append(nom)
        esta = float(input("Ingrese su estatura: "))
        listesta.append(esta)
        edad = int(input("Ingrese su edad: "))
        listedad.append(edad)
    print("\nListas registradas:")
    print("Nombres:", listnom)
    print("Estaturas:", listesta)
    print("Edades:", listedad)
    print(f"La longitud de la lista de edades es: {len(listedad)}")
    listnom.pop(2)
    listesta.pop(2)
    listedad.pop(2)
    listnom.append("Carlos")
    listesta.append(1.89)
    listedad.append(35)
    Angela_Martinez = listnom + listesta + listedad
    print("\nNueva lista unida (Angela_Martinez):")
    print(Angela_Martinez)
    opc = input("\n¿Desea registrar nuevamente? (S para salir): ")
print("Saliendo del programa...")