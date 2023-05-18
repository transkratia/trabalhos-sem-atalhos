# Implementar um programa que leia 10 valores inteiros via teclado, e como saída, exiba na tela o resultado da soma.

ciclo = 0
numTotal = 0

while ciclo < 5:
    numVariável = int(input("Fale um número. "))
    numTotal += numVariável
    ciclo += 1

print(f"A soma é igual a {numTotal}.")