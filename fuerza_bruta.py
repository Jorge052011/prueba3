import string
import getpass

contrasena_ingresada = getpass.getpass("Ingrese la contraseña que solo deben ser letras: ")

contrasena_minusculas = contrasena_ingresada.lower()
contador_intentos = 0

alfabeto = string.ascii_lowercase

for caracter_contrasena in contrasena_minusculas:
    
    for caracter_alfabeto in alfabeto:
        
        contador_intentos += 1
        if caracter_contrasena == caracter_alfabeto:
            break
        
            

print(f"La contraseña fue forzada en {contador_intentos} intentos")