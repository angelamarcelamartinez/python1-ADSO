print("--------------------\n")
print("Metodos de envio")
print("1.GET")
print("2.POST")
print("3.PUT")
print("4.DELETE")
print("5.SALIR")
print("--------------------\n")

method =int(input("Escribe el método HTTP: ")) 
print("--------------------\n")

while method != 5: 
    match method:
       case 1:
        print("GET- Fetching resource...")
       case 2:
        print("POST-Creating resource...")
       case 3:
        print("PUT-Updating resource...")
       case 4:
        print("DELETE-Deleting resource...")
       case _:
        print("Unsupported HTTP method")
    print("--------------------\n")
    print("Metodos de envio")
    print("1.GET")
    print("2.POST")
    print("3.PUT")
    print("4.DELETE")
    print("5.SALIR")
    print("--------------------\n")
    method =int(input("Escribe el método HTTP: ")) 
print("Usted salio")



 