# Implementar uma função que receba dois valores reais como parâmetro, correspondentes aos
# valores de base b e altura h de um triângulo, em seguida, calcule a área do triângulo a ( de
# acordo com a fórmula: a = b × h), e como saída, retorne o resultado.

def calcular_area_retangulo(b, h):
    area = b * h
    return area

resultado = calcular_area_retangulo(5, 3)
print("A área do retângulo é:", resultado)
