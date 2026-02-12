edad=int(input("Ingrese su edad:_"))
while edad>=1:
    
    for x in range (1,edad+1):
     print("cumplio:",x,"años") 
    if edad>=18:
      print("Es mayor de edad")
    else:
        print("Es menor de edad")
    edad = int(input("Ingrese su edad de nuevo:_"))
