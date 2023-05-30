# Implementar uma função que receba dois valores reais como parâmetros, correspondentes aos
# valores de base b e altura h do retângulo, em seguida, calcule a área do retângulo a (de acordo
# com a fórmula: a = b × h), e como saída, retorne o resultado

def calcular_area_retangulo(b, h):
    area = b * h
    return area

resultado = calcular_area_retangulo(5, 3)
print("A área do retângulo é:", resultado)
