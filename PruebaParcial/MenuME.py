import csv
import MenuPrincipal

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
    Estratificacion("BaseDeDatos_EII.csv", "Estrato1.csv", 5, lambda salario: int(salario) <= 5000)
    Estratificacion("BaseDeDatos_EII.csv", "Estrato2.csv", 5, lambda salario: int(salario) > 5000 and int(salario) <= 10000)
    Estratificacion("BaseDeDatos_EII.csv", "Estrato3.csv", 5, lambda salario: int(salario) > 10000)


CrearEstratos()

# Función para calcular el número de población (según estratos).
def numeroPoblacion(ruta):
    with open(ruta, "r", encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        contador = 0
        for item in range(len(ruta)):
            contador += 1
    return contador            


print(numeroPoblacion("SalarioMayor10000.csv"))
print(numeroPoblacion("SalarioMayor10000.csv"))

# Menú para el muestreo estratificado con asignación proporcional.
def MenuMuestreo():
    while True:
        try:
            print("----- MENÚ MUESTREO ESTRATIFICADO CON ASIGNACIÓN PROPORCIONAL -----")
            print("1. Estratificar.")

            option = int(input("Seleccione una opción: "))
            
        except ValueError:
            print("Ingrese un valor númerico.")

# Función para realizar las estratificaciones




'''
def Estratificacion(bd, ruta, elemento, condicion):
    bd = "BaseDeDatos_EII.csv"
    with open(ruta, "f", encoding = "utf-8") as file:
        for fila in bd[5]:
            if bd[5] < condicion:
                ruta.append(bd[5])
'''