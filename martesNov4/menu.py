print("Bienvenida a la tienda de maquillaje")

print("1 - Labial ($4000)")
print("2 - Polvo compacto ($6000)")
print("3 - Delineador ($3000)")
print("S - Salir")

total = 0

while True:
    opcion = input("Elige una opción: ").upper()

    if opcion == "S":
        break
    elif opcion == "1":
        total += 4000
        print("Agregaste un labial.")
    elif opcion == "2":
        total += 6000
        print("Agregaste un polvo compacto.")
    elif opcion == "3":
        total += 3000
        print("Agregaste un delineador.")
    else:
        print("Opción no válida.")

# Promoción
if total > 10000:
    descuento = total * 0.10
    total -= descuento
    print(f"\¡Felicidades! Se aplicó un 10% de descuento (${int(descuento)}).")

print("\nTotal a pagar: $", int(total))
print("¡Gracias por tu compra!")
