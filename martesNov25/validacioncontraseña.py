especiales = "@$!%*?&"

while True:
    clave = input("Escriba una contraseña: ")

    tiene_mayus = False
    tiene_especial = False
    suficiente_largo = False
    tiene_numero = False

    if len(clave) >= 8:
        suficiente_largo = True

    for a in clave:
        if a == a.upper():
            tiene_mayus = True
        if a in especiales:
            tiene_especial = True
        if a >= "0" and a <= "9":
            tiene_numero = True
            
    if tiene_mayus and tiene_especial and suficiente_largo and tiene_numero:
        print("Contraseña válida")
        break
    else:
        print("\nContraseña inválida")
        print("Debe tener:")
        print("- Una letra mayúscula")
        print("- Un carácter especial (@$!%*?&)")
        print("- Un número")
        print("- Mínimo 8 caracteres\n")
        
        #condicion segun el requisito, que la primera letra debe ser mayuscula, que la tercera letra mayuscula, que la 5 deba ser un caracter especia, que deba por ejemplo en numero 
 #alide segun la posicion 