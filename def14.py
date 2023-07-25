# Implementar uma função que receba um valor inteiro via teclado, em seguida, verifique se o valor
# é primo ou não (O número é primo quando é divisível por um e por ele mesmo), e como saída,
# retorne um valor lógico (verdadeiro para primo ou falso caso contrário)

def verificar_numero_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro: "))
resultado = verificar_numero_primo(numero)
if resultado:
    print("O número é primo!")
else:
    print("O número não é primo!")
