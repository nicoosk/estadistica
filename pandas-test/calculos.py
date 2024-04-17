import numpy as np

# Lee una sola columna del archivo CSV
columna = np.genfromtxt('high-diamond-10-min.csv', delimiter=',', usecols=(1,), skip_header=1)

# Muestra los primeros valores de la columna
print(columna)

# Si solo quieres acceder a los valores de la columna como una lista
valores_columna = columna.tolist()
print(valores_columna)
