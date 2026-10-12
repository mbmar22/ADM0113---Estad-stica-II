import csv
import MenuPrincipal
import sys
from pathlib import Path

# Para guardar los archivos dentro de la carpeta "Archivos".
ARCHIVOS_DIR = Path(__file__).resolve().parent / "Archivos"
CSV_BASE_DATOS = ARCHIVOS_DIR / "BaseDeDatos_EII.csv"
RUTA_E1 = ARCHIVOS_DIR / "Estrato1.csv"
RUTA_E2 = ARCHIVOS_DIR / "Estrato2.csv"
RUTA_E3 = ARCHIVOS_DIR / "Estrato3.csv"

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
    ARCHIVOS_DIR.mkdir(parents=True, exist_ok=True)
    # csvChat = "base_datos_estadistica_II.csv"
    Estratificacion(CSV_BASE_DATOS, RUTA_E1, 5, lambda salario: int(salario) <= 5000)
    Estratificacion(CSV_BASE_DATOS, RUTA_E2, 5, lambda salario: int(salario) > 5000 and int(salario) <= 10000)
    Estratificacion(CSV_BASE_DATOS, RUTA_E3, 5, lambda salario: int(salario) > 10000)


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


CrearEstratos()

# Función para imprimir los números de población. Podría juntarse con numeroPoblacion(), pero se va a dejar de esta manera por ahora.
def PrintNumeroPoblacion():
    estrato1 = numeroPoblacion(RUTA_E1)
    estrato2 = numeroPoblacion(RUTA_E2)
    estrato3 = numeroPoblacion(RUTA_E3)

    print(f"El estrato 1 (x1 <= a 5000) tiene {estrato1} elementos." )
    print(f"El estrato 2 (5000 < x2 <= 10000) tiene {estrato2} elementos." )
    print(f"El estrato 3 (x3 < 10000) tiene {estrato3} elementos." )
    print(f"En total hay una población de {estrato1 + estrato2 + estrato3}.\n")

    alto()

def alto():
    alto = input("Presione enter para regresar al menú principal...  ")


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
    print("----------   ESTRATIFICACIÓN DE SALARIO   ----------")
    salto()


    organizarPoblaciones(RUTA_E1, "X1 <= 5000 (C$)")

    salto()

    organizarPoblaciones(RUTA_E2, "5000 < X2 <= 10000 (C$)")

    salto()

    organizarPoblaciones(RUTA_E3, "X3 > 1000 (C$)")

    salto()

    PrintNumeroPoblacion()

# ------------------------------------------------------------------------------------

def EncontrarNumerosEstrato(nombreEstrato, estrato):
    nombreEstrato = nombreEstrato.capitalize()
    print(f"--- {nombreEstrato} ---")
    print("{nombreEstrato} tiene {filas} filas y {columnas} columnas.")
    print("Si desea salir y avanzar, escriba 's'")

    contador = 1
    lista = []

    while True:
        num = input(f"{contador}. Número aleatorio: ")
        if str(num).lower() == "s":
            break
        try:
            entrada = int(num)

            estratoElegido = (numeroPoblacion(estrato))
    
            if entrada > estratoElegido or entrada < 1:
                print(f"El número debe de estar entre 0 y {estratoElegido}.\n")
            else:
                lista.append((contador, num))
                contador += 1
        except ValueError:
            print("Ingrese un valor númerico entero.\n")

    return lista
            

def Calcular():
    MenuPrincipal.clearTerminal()
    print("\n--- Tamaño de muestra por estrato ---")
    print(EncontrarNumerosEstrato("Estrato 1", RUTA_E1))
    print(EncontrarNumerosEstrato("Estrato 2", RUTA_E1))
    print(EncontrarNumerosEstrato("Estrato 3", RUTA_E1))
    alto()

# ------------------------------------------------------------------------------------

# Menú para el muestreo estratificado con asignación proporcional.
def MenuMuestreo():
    while True:
        try:
            MenuPrincipal.clearTerminal()
            print("----- MENÚ MUESTREO ESTRATIFICADO CON ASIGNACIÓN PROPORCIONAL -----")
            print("1. Ver estratos." \
            "\n2. Calcular." \
            "\n3. Salir")

            option = int(input("Seleccione una opción: "))

            MenuPrincipal.SelectMenuOption(option, 1, PrintPoblaciones)
            MenuPrincipal.SelectMenuOption(option, 2, Calcular)
            MenuPrincipal.SelectMenuOption(option, 3, sys.exit)
            
        except ValueError:
            print("Ingrese un valor númerico.")


# Tal vez añadir una opción que permita buscar datos específicos. Ya sea de la base de datos principal o por estrato.

# Organizar las variables.