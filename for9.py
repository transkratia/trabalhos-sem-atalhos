# Implementar um programa que leia um valor inteiro via teclado, em seguida, calcule o fatorial de
# um número (O fatorial de 5! = 5 × 4 × 3 × 2 × 1 = 120), e como saída, exiba na tela o resultado.

numero = int(input("Fatorial de: ") )

resultado=1
for n in range(1,numero+1):
    resultado *= n

print(resultado)