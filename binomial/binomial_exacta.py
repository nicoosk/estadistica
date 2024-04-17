from scipy.stats import binom

# Parámetros
n = 4  # Número de ensayos totales
p = 0.7  # Probabilidad 
k = 4  # Número de éxitos

# Calculamos la probabilidad
prob = binom.pmf(k, n, p)
print(f"La probabilidad exacta de k: {k}, n: {n}, y p: {p} es: {prob}")
