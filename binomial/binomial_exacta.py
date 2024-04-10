from scipy.stats import binom

# Parámetros
n = 4  # Número de ensayos totales
p = 0.5  # Probabilidad de que ocurra el suceso
k = 2  # Número de éxitos deseados

# Calculamos la probabilidad
prob = binom.pmf(k, n, p)
print(f"La probabilidad exacta de {k} en los {n} usuarios es: {prob:.4f}")
