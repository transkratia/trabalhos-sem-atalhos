# Implementar um programa que leia 20 valores reais via teclado, e como saída, exiba na tela o
# resultado da média.

ciclo = 0
numTotal = 0

while ciclo < 20:
    numVariável = float(input("Fale um número. "))
    numTotal += numVariável
    ciclo += 1

print(f"A média é igual a {numTotal/20}.")