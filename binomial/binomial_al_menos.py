from scipy.stats import binom

# Parámetros
n = 4  # Número de ensayos totales
p = 0.5  # Probabilidad de que ocurra el suceso
al_menos = 2 # Condición que nos pide el ejercicio 

# Calculamos la probabilidad de al menos 2 
prob_al_menos_2 = sum(binom.pmf(k, n, p) for k in range(al_menos, n+1))
print(f"La probabilidad de que sea al menos {al_menos} de los {n} es: {prob_al_menos_2:.4f}")