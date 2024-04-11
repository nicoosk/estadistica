# Parámetros
x = 3.5 # Valor de variable a estandarizar
u = 3.1 # Media de X
sigma = 0.8 # Desviación estándar de X

# Estandarizamos X
z = (x - u)/sigma
print(f"El valor estandariado de {x} es: {z:.4f}")