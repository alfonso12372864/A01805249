#EJERCICIO 1 
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres adulto")
else:
    print("No eres adulto")

#EJERCICIO 2 
edad = int(input("Ingresa tu edad: "))

if edad >= 13 and edad <= 19:
    print("Eres adolescente")
else:
    print("No eres adolescente")

#EJERCICIO 3
nacimiento = int(input("Ingresa tu año de nacimiento: "))
edad = 2025 - nacimiento
print("Tienes", edad, "años")
