#ejercicio 1

temps = [20, 22, 25, 19, 30, 55, 21]

suma = 0
for t in temps:
    suma = suma + t

promedio = suma / len(temps)
print("Temperatura promedio:", promedio)

for i in range(len(temps)):
    if temps[i] > promedio:
        print("Día", i+1, "arriba de la media")
    else:
        print("Día", i+1, "abajo de la media")

#ejercicio 2 

alumnos = ["Paolo Peláez", "Patricio Muñoz", "Gonzalo García", "Diego Cuevas", "Maya Gutierrez", "Alfonso Abrajan"]
califs = [9, 5, 7, 4, 10, 6]

suma = 0
for c in califs:
    suma = suma + c

promedio = suma / len(califs)
print("Calificación promedio:", promedio)

reprobados = []
for i in range(len(califs)):
    if califs[i] < 7:
        reprobados.append(alumnos[i])

print("Reprobados:", reprobados)

aprobados = 0
for c in califs:
    if c >= 7:
        aprobados = aprobados + 1

porcentaje = (aprobados / len(califs)) * 100
print("Porcentaje de aprobados:", porcentaje, "%")

#ejercicio 3


listaCompras = ["gatorade","cervezas","carne"]
estadoCompras = [False,False,False]

for i in range(len(listaCompras)):
    if estadoCompras[i] == False:
        respuesta = input("¿Ya compraste " + listaCompras[i] + "? (si/no): ")
        if respuesta == "si":
            estadoCompras[i] = True

print("Estado de las compras:", estadoCompras)



#ejercicio4


numerosRandom = [8,2,15,4,7,1,10]

print("Número más grande:", max(numerosRandom))
print("Número más chico:", min(numerosRandom))

numerosRandom.sort()
print("Lista ordenada:", numerosRandom)


#ejercicio 5

listaNumeros = [1,2,3,4,5,6,7,8,9,10]

soloPares = []
soloImpares = []

for numero in listaNumeros:
    if numero % 2 == 0:
        soloPares = soloPares + [numero]
    else:
        soloImpares = soloImpares + [numero]

print("Números pares:", soloPares)
print("Números impares:", soloImpares)


#ejercicio6

usuariosRegistrados = ["Alfonso","Cuevas","Pato"]

nuevoUsuario = input("Ingresa un nombre de usuario: ")

while nuevoUsuario in usuariosRegistrados:
    print("Ese usuario ya existe, intenta con otro.")
    nuevoUsuario = input("Ingresa un nombre de usuario: ")

usuariosRegistrados = usuariosRegistrados + [nuevoUsuario]
print("Usuarios registrados:", usuariosRegistrados)

