# Implementar um programa que leia um valor inteiro via teclado, e como saída, exibir na tela se
# o valor é primo ou não (O número é primo quando é divisível por um e por ele mesmo).

def is_primo(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

n = int(input("Digite um número inteiro: "))

if is_primo(n):
    print(f"{n} é um número primo!")
else:
    print(f"{n} não é um número primo!")
