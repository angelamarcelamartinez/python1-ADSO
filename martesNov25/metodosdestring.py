palabra = "De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2025"
# Convierte todo a MAYÚSCULAS
print(palabra.upper()) 
print(palabra)  
# Convierte todo a minúsculas
print(palabra.lower())
print(palabra)     
# Pone la primera letra en mayúscula
print(palabra.capitalize()) 
print(palabra)    
# Pone mayúscula en la primera letra de cada palabra
print(palabra.title())
print(palabra)    
# Quita espacios al inicio y al final
print(palabra.strip())  
print(palabra)   
# Reemplaza una parte del texto por otra
print(palabra.replace("stephen", "ANGELA"))    
print(palabra)  
# BUSCAR dentro del string → devuelve posición
print(palabra.find("Sat"))     
print(palabra)  
# Cuenta cuántas veces aparece un valor
print(palabra.count("a")) 
print(palabra)       
# Verifica si todos los caracteres son dígitos
print(palabra.isdigit())   
print(palabra)      
# Verifica si todos los caracteres son letras
print(palabra.isalpha())   
print(palabra)      
# Verifica si son letras o números
print(palabra.isalnum())    
print(palabra)     
# Verifica si empieza con un texto específico
print(palabra.startswith("De")) 
print(palabra)  
# Verifica si termina con un texto específico
print(palabra.endswith("2025")) 
print(palabra)  
# Divide el
print(palabra.split())   
print(palabra)        
# Une elementos de una lista en un string
lista = ["Hola", "Mundo"]
print(" ".join(lista))     # Une usando un espacio
print(palabra)  