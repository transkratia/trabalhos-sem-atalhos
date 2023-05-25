# Implementar um programa que leia um valor inteiro via teclado, que corresponde o número de
# termos de uma série de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...), e como saída, exiba na tela
# cada valor da sequência.

n = int(input("Que termo deseja encontrar: "))

ultimo=1
penultimo=1

if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)

