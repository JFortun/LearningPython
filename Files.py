import statistics
from random import *

# Pido al usuario el nombre del archivo
nombreArchivo = (input("Escribe el nombre del archivo que quieres crear: "))

# Pido al usuario los nombres de las características y sus valores máximos y mínimos
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

# Creo las listas en las que se van a guardar los datos
datosCaract1 = []
datosCaract2 = []
datosCaract3 = []
datosCaract4 = []
datosCaract5 = []

# Creo cinco funciones que devuelven un número aleatorio comprendido entre los valores máximos y mínimos provistos por
# el usuario y guardan dicho número en su correspondiente lista


def funcion1():
    numero = str(randint(caract1Min, caract1Max))
    datosCaract1.append(numero)
    return numero


def funcion2():
    numero = str(randint(caract2Min, caract2Max))
    datosCaract2.append(numero)
    return numero


def funcion3():
    numero = str(randint(caract3Min, caract3Max))
    datosCaract3.append(numero)
    return numero


def funcion4():
    numero = str(randint(caract4Min, caract4Max))
    datosCaract4.append(numero)
    return numero


def funcion5():
    numero = str(randint(caract5Min, caract5Max))
    datosCaract5.append(numero)
    return numero

# Creo cinco funciones que sacan la media, moda, máximo, mínimo y varianza de cada lista de datos. En caso necesario
# se redondea con dos decimales para evitar números demasiado grandes


def media(datos):
    numero = statistics.mean(list(map(int, datos)))
    return str(round(numero, 2))


def moda(datos):
    numero = statistics.mode(list(map(int, datos)))
    return str(numero)


def maximo(datos):
    numero = max(list(map(int, datos)))
    return str(numero)


def minimo(datos):
    numero = min(list(map(int, datos)))
    return str(numero)


def varianza(datos):
    numero = statistics.variance(list(map(int, datos)))
    return str(round(numero, 2))


# Creo el fichero con el nombre indicado por el usuario
f = open(nombreArchivo + ".txt", "x")

# Creo el encabezado del archivo de texto que muestra las cinco características
encabezadoArchivo = caract1 + " | " + caract2 + " | " + caract3 + " | " + caract4 + " | " + caract5 \
    + "\n------------------------------------------------------------------------------------------"

# Añado texto al fichero
f.write(encabezadoArchivo + "\n")

# Cierro el fichero
f.close()

# Creo un bucle en el que en cada pasada se llama a las funciones que generan el número aleatorio. El iterador es 500
# en vez de 1000 porque se ejecuta dos veces por vuelta, así que genera las 1000 líneas correctamente
i = 1
while i < 500:
    f = open(nombreArchivo + ".txt", "a")
    texto = funcion1() + "       |      " + funcion2() + "       |      " + funcion3() \
        + "       |      " + funcion4() + "       |      " + funcion5() + "\n" \
        + "------------------------------------------------------------------------------------------ \n"

    # Escribo en el texto la línea generada en la instrucción anterior
    f.write(texto)
    i += 1

    # Cierro el fichero
    f.close()

# Muestro los resultados estadísticos de los datos obtenidos en las listas llamando a sus funciones correspondientes y
# pasando como parámetro la lista adecuada
print("                             ----- DATOS ESTADÍSTICOS -----\n" + "          " + encabezadoArchivo + "\n"
      + "MEDIA    | " + media(datosCaract1) + "   |   " + media(datosCaract2) + "   |  " + media(datosCaract3) + "   |  " + media(datosCaract4) + "   |  " + media(datosCaract5) + "\n"
      + "MODA     | " + moda(datosCaract1) + "   |   " + moda(datosCaract2) + "   |  " + moda(datosCaract3) + "   |  " + moda(datosCaract4) + "   |  " + moda(datosCaract5) + "\n"
      + "MÁXIMO   | " + maximo(datosCaract1) + "   |   " + maximo(datosCaract2) + "   |  " + maximo(datosCaract3) + "   |  " + maximo(datosCaract4) + "   |  " + maximo(datosCaract5) + "\n"
      + "MÍNIMO   | " + minimo(datosCaract1) + "   |   " + minimo(datosCaract2) + "   |  " + minimo(datosCaract3) + "   |  " + minimo(datosCaract4) + "   |  " + minimo(datosCaract5) + "\n"
      + "VARIANZA | " + varianza(datosCaract1) + "   |   " + varianza(datosCaract2) + "   |  " + varianza(datosCaract3) + "   |  " + varianza(datosCaract4) + "   |  " + varianza(datosCaract5))
