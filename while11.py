# Implementar um programa que leia um valor inteiro via teclado, e como saída, exibir na tela se
# o valor é primo ou não (O número é primo quando é divisível por um e por ele mesmo).

num = int(input("Digite um número. "))

flag = False

if num == 1:
    print(f"{num} não é primo.")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print(f"{num} não é primo.")
    else:
        print(f"{num} é primo.")