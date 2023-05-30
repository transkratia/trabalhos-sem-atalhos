# Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa
# anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de
# crescimento de 1.5%. Implemente um programa que exiba na tela o valor de crescimento de cada
# país ao ano até que país A ultrapasse ou iguale a população do país B.

populacao_A = 80000
taxa_crescimento_A = 0.03

populacao_B = 200000
taxa_crescimento_B = 0.015

ano = 0

while populacao_A <= populacao_B:
    ano += 1
    crescimento_A = populacao_A * taxa_crescimento_A
    crescimento_B = populacao_B * taxa_crescimento_B

    populacao_A += crescimento_A
    populacao_B += crescimento_B

    print(f"Ano {ano}:")
    print(f"População A: {int(populacao_A)} habitantes")
    print(f"População B: {int(populacao_B)} habitantes")
    print("-------------------------")

print(f"A população de A ultrapassou ou igualou a população de B no ano {ano}.")
