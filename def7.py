# Implementar uma função que receba um valor real como parâmetro, correspondente ao valor da
# base b do quadrado, em seguida, calcule a área do quadrado a (de acordo com a fórmula: a = b2),
# e como saída, retorne o resultado.

def calcular_area_quadrado(b):
    area = b ** 2
    return area

resultado = calcular_area_quadrado(5)
print("A área do quadrado é:", resultado)
