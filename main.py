import math
# k = Numero de éxitos deseados en los ensayos
# p = probabilidad de éxito en un ensayo (decimal)
# n = ensayos totales

k = 4
p = 0.3
n = 10

def calcularDistBinomial() -> float:
    coefBinomial = calcularCoefBinomial(n, k)
    return coefBinomial * (math.pow(p, k)) * math.pow((1 - p), (n - k))
    
    


def calcularCoefBinomial(n:int, k:int):
    factorialK = math.factorial(k)
    factorialN = math.factorial(n)
    return factorialN / (factorialK * math.factorial((n - k)))

print(calcularDistBinomial())
    