# Implementar uma função que receba dois valores reais como parâmetro, correspondentes
# radicando n e a ordem x de uma raiz r, em seguida, calcule a raiz (de acordo com a fórmula:
# r = n 1/x ), e como saída, retorne o resultado.

def calcular_raiz(n, x):
    raiz = n ** (1 / x)
    return raiz


