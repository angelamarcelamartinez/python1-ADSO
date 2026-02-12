# datos={9:{'name':'pepito','lastname':'tovar','pasw':'contraseÑ1.'}}
# last=datos[9]['lastname']
# for x in (last):
#     print(x)
# busc=int(input("Codigo a buscar:_"))
# while (busc in datos):
#    print(datos[busc]['name'])
#    break


#para llenar un diccionario vacio
colores={}
ingresar_color=input("Ingrese un color")
colores['color']=ingresar_color 
print("""
      '''''''menu principal'''''''
      1.ver diccionario
      2.editar diccionario
      3.eliminar
      0.salir
      """)
op=int(input("seleccione un opcion"))

if (op==1):
    print(colores)
#para editar el diccionario buscando entre las keys y los values
elif(op==2):
    for i,j in (colores.items()):
        print(f"keys {i} values {j}")
        busqueda_color=input("Ingrese el color a cambiar")
        if (busqueda_color==j):
            print(f"se encontro el color{busqueda_color}")
        else:
            print(f"nose encontro el color{busqueda_color}")
       

