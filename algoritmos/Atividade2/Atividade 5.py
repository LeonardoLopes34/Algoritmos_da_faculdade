funcionario=int(input("Insira o número do funcionário: " ))
horas=int(input("Insira o número de horas trabalhadas do funcionário: "))
salario_por_hora=float(input("Insira o valor que o funcionário recebe por hora: "))
resultado=float(salario_por_hora*horas)
round(resultado, 2)
print(f"O salário do funcionário {funcionario} é de R$:"+str(resultado))

