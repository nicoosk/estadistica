datos = [34,12,56,76,6,6,6,12,2,2,2,2,2,24,32] # Parámetros de entrada.

moda = 0
cantidad = 0
# Calculamos la moda
for numero in datos:
    if datos.count(numero) > datos[datos.index(numero) + 1]:
        print("Es mayor")
    else:
        print("Es menor")