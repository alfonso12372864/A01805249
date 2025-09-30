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


