from scipy.stats import binom

# Parámetros
n = 4  # Número de ensayos totales
p = 0.5  # Probabilidad de que ocurra el suceso

# Calculamos la probabilidad de al menos 2 
prob_al_menos_2 = sum(binom.pmf(k, n, p) for k in range(2, n+1))
print(f"La probabilidad de que al menos 2 de los {n} usuarios instalen la actualización es: {prob_al_menos_2:.4f}")