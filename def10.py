# Implementar uma função que receba um valor real como parâmetro, correspondente ao valor
# do raio r de um círculo, em seguida, calcule a área do círculo a (de acordo com a fórmula:
# a = 3.14r2), e como saída, retorno o resultado

def calcular_area_circulo(r):
    area = 3.14 * (r ** 2)
    return area

resultado = calcular_area_circulo(5)
print("A área do círculo é:", resultado)
