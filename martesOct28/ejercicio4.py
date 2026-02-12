num=int(input("Ingrese un numero:_"))
while num>=1:
   for x in range(1,num+1,2):
      print(x,end=",")
   num=int(input("\nIngrese un numero de nuevo:_"))