# Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa
# anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de
# crescimento de 1.5%. Implemente um programa que exiba na tela o valor de crescimento de cada
# país ao ano até que país A ultrapasse ou iguale a população do país B.

countryA = 80.000
countryB = 200.000

while countryA <= countryB:
    countryA += countryA * 0.03
    countryB += countryB * 0.015
    print(f"A população atual do país A é de {countryA}")
    print(f"A população atual do país B é de {countryB}")