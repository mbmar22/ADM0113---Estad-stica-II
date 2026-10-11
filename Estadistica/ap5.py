print("----- MUESTREO POR CONGLOMERADOS -----")

def options(option, numero, funcion):
    if option == numero:
        while True:
            funcion

'''def quit(option, number, function):
    if option == number:
        function'''

ai = []
yi = []


def validation(hola, funcion, mensaje):
    while True:
        if hola.upper() == "N":
            print(mensaje)
            break
        try:
            valor = float(hola)
            funcion
        except ValueError:
            print("Ingrese un valor númerico.\n")
            break


def menu_data(data):
    print(f"--- Opciones {data} ---")
    print(f"1. Añadir {data}.")
    print(f"2. Modificar {data}.")
    print(f"3. Eliminar {data}.")

    option = input("\nIngrese una opción: ")

    validation(option, add_element(data), "Regresando al menú principal.")
    option(option, 1, add_element(data))


def menu():
    while True:
        print("--- Menú principal ---")
        print("\n1. Opciones ai." \
        "\n2. Opciones yi." \
        "\n3. Mostrar tabla de datos." \
        "\n4. Calcular." \
        "\n5. Salir.")

        option = input("Ingrese una opción: ")

        options(option, 1, menu_data("ai"))
        options(option, 2, menu_data("yi"))
        options(option, 3, read_data(ai))

        if option == 5:
            print("Saliendo del programa...")
            break


def read_data(list):
    for item in list:
        print("|" + item + "|")


def add_element(list):
    contador = 1
    print("- A partir de ahora ingrese ai o presione 'N' para salir -")
    while True:
        element = input(f"Ingrese el precio del conglomerado #{contador}: ")
        if element.upper() == "N":
            print("Fin del ingreso.")
            break
        try:
            valor = float(element)
            list.append(element)
            contador += 1
        except ValueError:
            print("Ingrese una cantidad o 'N' para salir.\n")
    menu()

menu()