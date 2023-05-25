# Implementar um programa que leia 10 valores inteiros via teclado, e como saída, exiba na tela o resultado da soma.

vSoma = 0

for i in range(0, 10, 1):
    vInt = int(input("Digite um valor. "))
    vSoma += vInt

print(f"A soma é igual a {vSoma}")