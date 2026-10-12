import time
import sys
import os
import MenuME, MenuPH, MenuPI
from colorama import Fore, Style, colorama_text, init # Ver después como adaptar esto en funciones.
init()

# Para repetir los "." al final.
def Repeat(message, repetitions, item):
    print("\n" + message, end = "")
    for i in range(repetitions):
        print(item, end = "", flush = True)
        time.sleep(0.1)
    print("\n")


# Función para escoger una función.
def SelectMenuOption(number, option, function):
    if number == option:
        if function == exiting:
            Repeat("Saliendo", 3, ".")
        else:
            Repeat(f"Redirigiendo a la opción {number}", 3, ".")
        clearTerminal()
        time.sleep(0.1)
        function()


# Función para resetear la terminal.
def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


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
            global exiting
            exiting = sys.exit

            SelectMenuOption(number, 1, MenuME.MenuMuestreo)
            SelectMenuOption(number, 2, MenuPH.MenuPHipotesis)
            SelectMenuOption(number, 3, MenuPI.MenuPIndependencia)
            SelectMenuOption(number, 4, exiting)

            if number < 1 or number > 4:
                print("Ingrese un número dentro del rango válido.")
    
        except ValueError:
            print("Error, ingrese un número válido.")