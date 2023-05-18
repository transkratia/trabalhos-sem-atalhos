# Implementar um programa que leia 15 valores inteiros via teclado, e como saída, exiba na tela o
# menor valor.

ciclo = 1
numMenor = 0
numTotal = int(input("Fale um número. "))

while ciclo < 15:
    numVariável = int(input("Fale um número. "))
    if numVariável < numTotal:
        numMenor = numVariável
    ciclo += 1

if numMenor < numTotal:
    print(f"O menor número é igual a {numMenor}.")
else:
    print(f"O menor número é igual a {numTotal}.")