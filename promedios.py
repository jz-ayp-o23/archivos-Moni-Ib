#Se abre el archivo en modo lectura
with open('data/calificaciones.txt', 'r') as alumnos:
    promedios = []
    for alumno in alumnos:
        individual = alumno.split()
        nombre = individual[0]
        apellido = individual[1]
        apellido_may = apellido.upper()
        calificaciones = [float(calificacion) for calificacion in individual[2:]]
        promedio = sum(calificaciones) / len(calificaciones)
        promedio_redondeado = round(promedio,1)
        promedios.append([nombre, apellido_may, promedio_redondeado])

#'data/promedios.txt' es el nombre del archivo de salida,
# Abrir el archivo de promedios en modo agregar ('a')
with open('data/promedios.txt', 'w') as final:
    for promedio in promedios:
        nombre = promedio[0]
        apellido = promedio[1]
        promedio_final = promedio[2]
#Se escribe una línea en el archivo promeidos con el formato "Apellido, Nombre: Promedio"
        final.write(f"{apellido}, {nombre}: {promedio_final:.1f}\n")


