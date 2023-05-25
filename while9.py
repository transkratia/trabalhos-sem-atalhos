# Implementar um programa que leia um valor inteiro via teclado, em seguida, calcule o fatorial de
# um número (O fatorial de 5! = 5 × 4 × 3 × 2 × 1 = 120), e como saída, exiba na tela o resultado.

n = int(input("Digite o fatorial: ") )
r = 1
counter = 1

while counter <= n:
    r *= counter
    counter += 1

print(f"O fatorial é de: {r}")