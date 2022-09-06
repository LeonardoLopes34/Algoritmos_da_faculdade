peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu altura: "))

imc = peso/altura**2
arrendondado = round(imc, 2)

print(imc)

if imc < 17:
    print(f"Seu IMC é:", arrendondado , "e está classificado como MUITO ABAIXO DO PESO")
elif arrendondado > 17 and arrendondado < 18.49:
    print("Seu IMC é:", arrendondado , "e está classificado como ABAIXO DO PESO")
elif arrendondado >= 18.5 and arrendondado < 24.99:
    print("Seu IMC é:", arrendondado , "e está classificado como PESO NORMAL")
elif arrendondado >= 25 and arrendondado < 29.99:
    print("Seu IMC é:", arrendondado , "e está classificado como ACIMA DO PESO")
elif arrendondado >= 30 and arrendondado < 34.99:
    print("Seu IMC é:", arrendondado , "e está classificado como OBESIDADE I")
elif arrendondado >= 35 and arrendondado < 39.99:
    print("Seu IMC é:", arrendondado , "e está classificado como OBESIDADE II")
else:
    print("Seu IMC é:", arrendondado , "e está classificado como OBESIDADE III")