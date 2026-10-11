import time
import sys

# Función para el menú principal.
def MainMenu():
    while True:
        try:
            print("\n----- BIENVENIDO AL PROGRAMA DE ESTADÍSTICA II -----")
            print("Opciones:" \
            "\n1. Problema de muestreo estratificado." \
            "\n2. Problema de prueba de hipótesis." \
            "\n3. Problema de prueba de independencia." \
            "\n4. Salir.") 

            number = int(input("\nIngrese una opción: "))

            SelectMenuOption(number, 1, lambda: print("Hola"))
            SelectMenuOption(number, 2, lambda: print("Hey!"))
            SelectMenuOption(number, 3, lambda: print("¡¿Qué?!"))
            SelectMenuOption(number, 4, lambda: sys.exit())

            if number < 1 or number > 4:
                print("Ingrese un número dentro del rango válido.")
    
        except ValueError:
            print("Error, ingrese un número válido.")

# Función para escoger una función.
def SelectMenuOption(number, option, function):
    if number == option:
        if function == [lambda: sys.exit()]:
            print("Saliendo del programa...")
        else:
            print(f"Redirigiendo a la la opción {number}...")
        time.sleep(1)
        function()