# Implementar uma função que receba um valor inteiro via teclado, correspondente ao valor do
# ano, em seguida, verifique se o ano é bissexto ou não, e como saída, retorne um resultado lógico
# (verdadeiro para bissexto ou falso caso contrário).

def verificar_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano = int(input("Digite o ano: "))
resultado = verificar_ano_bissexto(ano)
print("O ano é bissexto?", resultado)
