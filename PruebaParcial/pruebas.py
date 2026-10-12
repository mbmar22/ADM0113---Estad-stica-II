from MenuME import RUTA_E1, RUTA_E2, RUTA_E3

# Split into a list of integers
digits = [int(ch) for ch in ''.join(c for c in RUTA_E1.name if c.isdigit())]

print(digits[0])  # Output: [5, 9]
print(digits)

# Tal vez si convierto cada fila en una lista, con el contador en 0, luego según el otro dígito lo ubico. Por ejemplo:
'''
Por ejemplo:
estrato = RUTA_E1
convertir a lista el estrato
contador = 0
numeroDadoPorElUsuario = 59

separacion = [5, 9] - Otra cosa, el que debe de quedar solo es el último, por ejemplo 115 [11, 5]
for row in range(len(estrato[0]))
    if contador == separacion[0]:
        for column in range(len("Estrato1.csv"))

    contador += 1



        
        contador2 += 1
        if 
        estrato.append()
    contador += 1

O sea, recorrer todas las filas hasta encontrar el match con separacion[0], y luego recorrer las columnas para encontrar el match con separacion[1], y de ahí hacer el append.

'''