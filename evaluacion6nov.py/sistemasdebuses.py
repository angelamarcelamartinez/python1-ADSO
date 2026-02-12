r1_personas=0
r2_personas=0
r3_personas=0
r4_personas=0
r5_personas=0

tari1=2000
tari2=2000
tari3=2000
tari4=2000
tari5=2000

subtotal=0

print("Selecione LA RUTA que desee")
print("--------------------\n")
print("1.LA RUTA 1, PANAMERICANA,CENTRO COMERCIAL AQUA, LA ESTACION, UNIVERSIDAD DE IBAGUE")
print("2.LA RUTA 2, PISCINAS OLIMPICAS,CENTRO COMERCIAL LA QUINTA, CATEDRAL, LA CUN")
print("3.LA RUTA 8, PISCINAS OLIMPICAS,CENTRO COMERCIAL LA QUINTA, CATEDRAL, PANOPTICO")
print("4.LA RUTA 21, MULTICENTRO, MERCACENTRO,SUTIPLAZA, EL SALADO")
print("5.LA RUTA 40, PISCINAS OLIMPICAS,CATEDRAL, CALLE 15,RICAURTE")
print("--------------------\n")
print("6.SALIR")
print("--------------------\n")

opc=int(input("Ingrese una opcion"))
while opc !=6:
    match opc:
       case 1:
          print("RUTA 1")
       case 2:
              print("RUTA 2")
       case 3:
          print("RUTA 8")
       case 4:
          print("RUTA 21")
       case 5:
          print("RUTA 40")
       case 6:
          print("Unsupported HTTP method")