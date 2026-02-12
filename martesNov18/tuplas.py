a=([10,5,"adso"]),{"doc":110223,"nom":"Cesar"},(2,5,True)
print(a[1]["nom"])
mitupla=(["Angela","Marcela","Martinez","Ruiz"],(18,19,20,21),["Azul","Negro"],("Luna","Mar"))
print(mitupla[2])
A=("a",1,"i",2,"u",3,"o")
print(A[3:])#imprimir desde la posicion 3 hasta la 6
print(A[:4])#imprimir desde la posicion 0 hasta la 4 
print(A[:5:2])#5 la posicion en la que empieza y 2 el salto 
print(A[::2])#salto en 2 solamente
print(A[1::2])#1 donde empieza y  el salto 

a=(2,5,tuple)
b=list(a)
b.append(109)
b[0]=900
a=tuple(b)
print(b)
print(a)

a=(2,5,3)
b=[]
for i in (a):
    b.append(i)
print(b)

a=([10,5,"adso"],{"doc":110223,"nom":"Cesar"},(2,5,True))
a[0][2]="Adso 2901879"
print(a[0])

a=([10,5,"adso"],{"doc":110223,"nom":"Cesar"},(2,5,True))
a[1]["doc"]=1234567
print(a[1])
