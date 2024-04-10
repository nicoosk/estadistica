from scipy.stats import binom

# Parámetros
n = 4  # Número de ensayos totales
p = 0.5  # Probabilidad de que ocurra el suceso

# Calculamos la probabilidad de más de 2 
prob_mas_de_2 = sum(binom.pmf(k, n, p) for k in range(3, n+1))
print(f"La probabilidad de que más de 2 de los {n} usuarios instalen la actualización es: {prob_mas_de_2:.4f}")