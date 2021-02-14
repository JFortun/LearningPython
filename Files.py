from random import *

# Pido al usuario los datos necesarios
nombreArchivo = (input("Escribe el nombre del archivo que quieres crear: "))
caract1 = (input("Escribe la característica 1: "))
caract1Max = int(input("Indica el valor máximo de " + caract1 + ": "))
caract1Min = int(input("Indica el valor mínimo de " + caract1 + ": "))
caract2 = (input("Escribe la característica 2: "))
caract2Max = int(input("Indica el valor máximo de " + caract2 + ": "))
caract2Min = int(input("Indica el valor mínimo de " + caract2 + ": "))
caract3 = (input("Escribe la característica 3: "))
caract3Max = int(input("Indica el valor máximo de " + caract3 + ": "))
caract3Min = int(input("Indica el valor mínimo de " + caract3 + ": "))
caract4 = (input("Escribe la característica 4: "))
caract4Max = int(input("Indica el valor máximo de " + caract4 + ": "))
caract4Min = int(input("Indica el valor mínimo de " + caract4 + ": "))
caract5 = (input("Escribe la característica 5: "))
caract5Max = int(input("Indica el valor máximo de " + caract5 + ": "))
caract5Min = int(input("Indica el valor mínimo de " + caract5 + ": "))

# Creo el fichero
f = open(nombreArchivo + ".txt", "x")
print("Fichero " + nombreArchivo + " creado.")
encabezadoArchivo = caract1 + " | " + caract2 + " | " + caract3 + " | " + caract4 + " | " + caract5
# Añado texto al fichero
f.write(encabezadoArchivo + "\n")
f.close()

i = 1
while i < 1000:
    f = open(nombreArchivo + ".txt", "a")
    texto = str(randint(caract1Min, caract1Max)) + "        |       " + str(randint(caract2Min, caract2Max)) \
            + "        |       " + str(randint(caract3Min, caract3Max)) \
            + "        |       " + str(randint(caract4Min, caract4Max)) \
            + "        |       " + str(randint(caract5Min, caract5Max)) + "\n"
    f.write(texto)
    i += 1
    f.close()
# Cierro el fichero
