import csv
import MenuPrincipal
import sys

# Función para realizar las estratificaciones
def Estratificacion(bd, ruta, element, condition):  # Define la función y sus parámetros.
    numbers = []

    with open(bd, "r", encoding = "utf-8") as file:
        reader = csv.reader(file)
        next(reader) # Para omitir la fila de los encabezados

        numbers.append(" ") # La ubicación 0, 0 se debe de quedar vac

        for row in reader:
            if condition(row[element]):
                numbers.append(row[element])

    matrix = []

    for i in range(0, len(numbers), 10):
        matrix.append(numbers[i:i+10])

    with open(ruta, "w", encoding = "utf-8", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(matrix)


# Crear los estratos.
def CrearEstratos():
    csvYo = "BaseDeDatos_EII.csv"
    # csvChat = "base_datos_estadistica_II.csv"
    Estratificacion(csvYo, "Estrato1.csv", 5, lambda salario: int(salario) <= 5000)
    Estratificacion(csvYo, "Estrato2.csv", 5, lambda salario: int(salario) > 5000 and int(salario) <= 10000)
    Estratificacion(csvYo, "Estrato3.csv", 5, lambda salario: int(salario) > 10000)


CrearEstratos()

# Función para calcular el número de población (según estratos).
def numeroPoblacion(ruta):
    with open(ruta, "r", encoding = "utf-8") as file:
        reader = csv.reader(file)
        contador = []
        quantity = -1

        for row in reader:
            #result = [x for x in contador if isinstance(x, (int, float))], ver si puedo hacer que no cuente los espacios vacíos. Por ahora nada más alterar el valor de quantity con - 1 o dejarlo en 0 y al final restarle 1.
            contador.append(len(row))

        for i in contador:
            quantity += i


    return quantity   

# Función para imprimir los números de población. Podría juntarse con numeroPoblacion(), pero se va a dejar de esta manera por ahora.
def PrintNumeroPoblacion():
    estrato1 = numeroPoblacion("Estrato1.csv")
    estrato2 = numeroPoblacion("Estrato2.csv")
    estrato3 = numeroPoblacion("Estrato3.csv")

    print(f"El estrato 1 (x1 <= a 5000) tiene {estrato1} elementos." )
    print(f"El estrato 2 (5000 < x2 <= 10000) tiene {estrato2} elementos." )
    print(f"El estrato 3 (x3 < 10000) tiene {estrato3} elementos." )
    print(f"En total hay una población de {estrato1 + estrato2 + estrato3}.\n")


def organizarPoblaciones(ruta, mensaje):
    tabla = []

    with open(ruta, "r") as file:
        reader = csv.reader(file)

        max = 0

        for row in reader:
            tabla.append(row)

            for x in row:
                if len(x) > max:
                    max = len(x)

        ancho = max + 2


        def long():
            algo = ("—" * ((ancho + 1) * (len(tabla[0]) + 1) + 1))
            print(algo)
            length = algo.count("—")

        length = (ancho + 1) * (len(tabla[0]) + 1) + 1
        print(mensaje.center(length))

        long()

        encabezado = ["No."] + list(range(len(tabla[0])))

        print("|" + "|".join(str(i).center(ancho) for i in encabezado) + "|")


        long()

        contador = 0

        for row in tabla:
            print("|" + str(contador).center(ancho) + "|" + 
                  "|".join(x.center(ancho) for x in row) + "|")
            long()

            contador += 1

    return tabla


def salto():
    print("\n")

def PrintPoblaciones():
    print("--- ESTRATIFICACIÓN DE SALARIOS ---")
    organizarPoblaciones("Estrato1.csv", "X1 <= 5000 (C$)")

    salto()

    organizarPoblaciones("Estrato2.csv", "5000 < X2 <= 10000 (C$)")

    salto()

    organizarPoblaciones("Estrato3.csv", "X3 > 1000 (C$)")

    salto()

    PrintNumeroPoblacion()


# Menú para el muestreo estratificado con asignación proporcional.
def MenuMuestreo():
    while True:
        try:
            print("----- MENÚ MUESTREO ESTRATIFICADO CON ASIGNACIÓN PROPORCIONAL -----")
            print("1. Ver estratos." \
            "\n2. Salir")

            option = int(input("Seleccione una opción: "))

            MenuPrincipal.SelectMenuOption(option, 1, PrintPoblaciones)
            MenuPrincipal.SelectMenuOption(option, 2, sys.exit)
            
        except ValueError:
            print("Ingrese un valor númerico.")

