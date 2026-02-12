especiales = ("@", "$", "!", "%", "*", "?", "&")
contrasenas = []
error = 0

print("Bienvenido a Facebook")

while True:
    print("\n--- MENÚ ---")
    print("1. Registrarse")
    print("2. Ver historial")
    print("3. Salir")
    opc = input("Escoja una opción: ")

    match opc:
        case "1":
            while True:
                contra = input("Digite su contraseña: ")

                reglas = {
                    "longitud": 8,
                    "mayus": True,
                    "mini": True,
                    "num": True,
                    "espe": True
                }

                mayus = False
                mini = False
                num = False
                espe = False
                errores = []

                if len(contra) < reglas["longitud"]:
                    errores.append(f"La contraseña debe tener al menos {reglas['longitud']} caracteres.")

                for x in contra:
                    if x.isupper():
                        mayus = True
                    if x.islower():
                        mini = True
                    if x in especiales:
                        espe = True
                    if x.isdigit():
                        num = True

                if reglas["mayus"] and not mayus:
                    errores.append("Debe tener al menos una letra mayúscula.")
                if reglas["mini"] and not mini:
                    errores.append("Debe tener al menos una letra minúscula.")
                if reglas["num"] and not num:
                    errores.append("Debe tener al menos un número.")
                if reglas["espe"] and not espe:
                    errores.append("Debe contener un carácter especial (@$!%*?&).")

                if errores:
                    print("\n Contraseña inválida. Errores:")
                    for e in errores:
                        print(" -", e)
                    error=error+1
                    continue
                else:
                    contrasenas.append(contra)
                    print("\nContraseña válida")
                    contrasenas.append(contra)

                    # Clasificación simple de nivel
                    if mayus and mini and num and espe and len(contra) >= 10:
                        nivel = "Fuerte"
                    elif (mayus or mini) and num:
                        nivel = "Media"
                    else:
                        nivel = "Débil"

                    match nivel:
                        case "Fuerte":
                            print("Nivel de seguridad: Fuerte")
                        case "Media":
                            print("Nivel de seguridad: Media")
                        case "Débil":
                            print("Nivel de seguridad: Débil")

                    break 

        case "2":
            print("\n--- HISTORIAL ---")
            if not contrasenas:
                print("No hay contraseñas registradas.")
            else:
                print(contrasenas)
                print("Errores cometidos:", error)

        case "3":
            print("\nSaliendo del sistema...")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")
