from scipy.stats import binom

# Parámetros
n = 4  # Número de ensayos totales
p = 0.5  # Probabilidad de que ocurra el suceso
mas_de = 3 # Condicion otorgada por el ejercicio. Si te pide que sea mas de, tienes que poner el numero + 1

# Calculamos la probabilidad de más de 2 
prob_mas_de_2 = sum(binom.pmf(k, n, p) for k in range(mas_de, n+1))
print(f"La probabilidad de más de 2 de los {n} usuarios es: {prob_mas_de_2:.4f}")