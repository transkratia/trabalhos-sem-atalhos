# Implementar um programa que leia dois valores inteiros via teclado, sendo o primeiro menor que
# o segundo, e como saída, exibir apenas os números primos do início ao fim da sequência.

low = int(input("Insira o primeiro número. "))
high = int(input("Insira o segundo número. "))

primes = []

for i in range(low, high + 1):
    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)
        
print(primes)