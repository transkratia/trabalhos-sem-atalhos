# Implementar um programa que leia um valor inteiro via teclado, que corresponde o número de
# termos de uma série de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...), e como saída, exiba na tela
# cada valor da sequência.

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        seq = [1, 1]
        while len(seq) < n:
            next_term = seq[-1] + seq[-2]
            seq.append(next_term)
        return seq

n = int(input("Digite o número de termos da sequência de Fibonacci: "))
sequencia = fibonacci(n)

print("Sequência de Fibonacci:")
for termo in sequencia:
    print(termo)
