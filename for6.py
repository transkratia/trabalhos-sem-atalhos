# Implementar um programa que leia 15 valores inteiros via teclado, e como saída, exiba na tela o menor valor.

numMenor = 0
numTotal = int(input("Fale um número. "))

for i in range(0, 15, 1):
    numVariável = int(input("Fale um número. "))
    if numVariável < numTotal:
        numMenor = numVariável

if numMenor < numTotal:
    print(f"O menor número é igual a {numMenor}.")
else:
    print(f"O menor número é igual a {numTotal}.")