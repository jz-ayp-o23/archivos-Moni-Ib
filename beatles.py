f = open("beatles.txt", "r", encoding = "utf8")
for linea in f:
    print(linea)
#Siempre hay que cerrar el archivo al terminar de trabajar con él
f.close()
