users = { 10901: {"nombre": "Catalina Forero", "contraseña": "Qwe1rt#a", "saldo": 10000}, 11123: {"nombre": "Miguel Triana", "contraseña": "A123bx$n", "saldo": 20000}}
consignaciones = []
retiros = []
print("Bienvenido, Tiene 3 oportunidades para ingresar credenciales")
sigue = False  
for x in range(3):
    cedula = int(input("Ingrese número de cédula: "))
    if cedula in users:
        contraseña = input("Ingrese su contraseña: ")
        if contraseña == users[cedula]["contraseña"]:
            print(f"Bienvenido/a {users[cedula]['nombre']}")
            sigue = True
            break  
        else:
            print("Contraseña incorrecta")
    else:
        print("Cédula no encontrada")

if not sigue:
    print("Suficientes intentos, saliendo del programa")
    exit()
else:
    opc = 0
    while opc != 5:
        print("""     Menu    
            1. Ver saldo
            2. Consignar
            3. Retirar
            4. Ver movimientos
            5. Salir """)
        opc = int(input("Ingrese la opción que desee: "))
        match opc:
            case 1:
                print(f"Su saldo es: {users[cedula]['saldo']}")
            case 2:
                monto = int(input("Ingrese el monto a consignar (minimo 5000): "))
                while monto < 5000:
                    print("El monto a consignar es inválido (mínimo 5000)")
                    monto = int(input("Ingrese el monto a consignar (minimo 5000): "))
                users[cedula]["saldo"] = users [cedula]["saldo"] + monto
                consignaciones.append(monto)
                print(f"Usted ha consignado {monto}, su nuevo saldo es {users[cedula]["saldo"]}")
            case 3:
                montoret = int(input("Ingrese el monto a retirar (minimo 5000): "))
                while montoret < 5000 or montoret > users[cedula]['saldo']:
                    print("Monto inválido.")
                    montoret = int(input("Ingrese el monto a retirar (minimo 5000): "))
                users[cedula]["saldo"] = users[cedula]["saldo"] - montoret
                retiros.append(montoret)
                print(f"Usted ha retirado {montoret}, su nuevo saldo es {users[cedula]["saldo"]}")
            case 4:
                print(f"Los retiros que ha realizado han sido {retiros}")
                print(f"Las consignaciones que ha realizado han sido {consignaciones}")
            case 5:
                print(f"Hasta pronto {users[cedula]["nombre"]}")
            case _:
                print("Opción inválida.")