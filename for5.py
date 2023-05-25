# Implementar um programa que leia 20 valores reais via teclado, e como saída, exiba na tela o resultado da média.

vSoma = 0

for i in range(0, 20, 1):
    vInt = int(input("Digite um valor. "))
    vSoma += vInt

print(f"A média é igual a {vSoma/20}")