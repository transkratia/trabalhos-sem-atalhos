# Implementar um programa que leia dois valores inteiros via teclado, sendo o primeiro menor que
# o segundo, e como saída, exibir apenas os números primos do início ao fim da sequência.

def is_primo(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

print(f"Números primos no intervalo de {inicio} a {fim}:")
for num in range(inicio, fim + 1):
    if is_primo(num):
        print(num)
