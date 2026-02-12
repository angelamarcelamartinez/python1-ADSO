acue=0
acua=0
perso=int(input("Ingrese total de personas:_"))
if perso<1:
    print("Error")
else:
    for x in range(1,perso+1):
      print("\nPersona numero ",x)
      nombre=str(input("Ingrese su nombre:_"))
      edad=int(input("Ingrese su edad:_"))
      altura=float(input("Ingrese su altura:_"))
      acue=acue+edad
      acua=acua+altura
    prome=acue/perso
    proma=acua/perso
        
    if prome<15 and proma <1.55:
        print("\n--- RESULTADOS ---") 
        print("El promedio de edad fue:_",prome,"El promedio de altura fue:_",proma)
        print("Su altura es un poco baja para la edad")
    elif prome>=15 and proma>=1.68:
        print("\n--- RESULTADOS ---") 
        print("El promedio de edad fue:_",prome,"El promedio de altura fue:_",proma)
        print("Usted va a ser alto")
    else: 
        print("\n--- RESULTADOS ---") 
        print("El promedio de edad fue:_",prome,"El promedio de altura fue:_",proma)
        print("El promedio es bueno")





