# Implementar uma função que receba um valor inteiro via teclado, em seguida, calcule
# recursivamente o fatorial (O fatorial de 5! = 5 × 4 × 3 × 2 × 1 = 120), e como saída, retorne o resultado

def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

numero = int(input("Digite um número inteiro: "))
resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "é:", resultado)
