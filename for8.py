# Implementar um programa que leia 10 valores reais via teclado, e como saída, exiba o menor valor, o maior valor e a média de todos os valores.

numMenor = 9999999999999999999999
numMaior = -999999999999999999999
# numTotal = int(input("Fale um número. "))
numMédio = 0

for i in range(0, 10, 1):
    numVariável = int(input("Digite um número. "))
    numMédio += numVariável
    if numVariável < numMenor:
        numMenor = numVariável
    if numVariável > numMaior:
        numMaior = numVariável

print(f"O menor valor é de {numMenor}, o maior valor é de {numMaior} e média é igual a: {numMédio/10}")