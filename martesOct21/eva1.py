print("🍉 Bienvenido a la tienda de frutas 🍉")

# Valores de cada fruta
valor_mango = 2500
valor_pera = 1800
valor_banano = 1200

# Variables acumuladoras
total_compra = 0
contador_compras = 0

while True:
    print("Menú de frutas:")
    print("1 - Mango")
    print("2 - Pera")
    print("3 - Banano")
    print("S - Salir")

    opcion = input("Elija una opción: ").upper()

    if opcion == "S":
        break
    elif opcion == "1":
        fruta = "Mango"
        precio = valor_mango
    elif opcion == "2":
        fruta = "Pera"
        precio = valor_pera
    elif opcion == "3":
        fruta = "Banano"
        precio = valor_banano
    else:
        print("Opción no válida. Intente de nuevo.")
        continue

    # Pedir cantidad
    cantidad = int(input(f"Ingrese la cantidad de {fruta}s que desea comprar: "))

    # Calcular subtotal
    subtotal = cantidad * precio
    total_compra += subtotal
    contador_compras += 1

    print(f"Has comprado {cantidad} {fruta}(s) por un total de $",subtotal)

# Al salir del ciclo
if contador_compras > 0:
    promedio = total_compra / contador_compras
    print("Resumen de compra:")
    print("Total de la compra: $",total_compra)
    print("Promedio por tipo de fruta: $",promedio)
else:
    print("No realizaste ninguna compra.")

print("Gracias por visitar la tienda de frutas!")
