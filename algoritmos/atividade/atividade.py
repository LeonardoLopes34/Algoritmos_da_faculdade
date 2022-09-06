numero_um = int(input('Insira o primeiro número: '))
numero_dois = int(input('Insira o segundo número: '))

numero_um%2 , numero_dois%2
numero_um%2 , numero_dois%2

menor_que = numero_um < 10
maior_que =numero_dois > 10

numero_ao_quadrado = numero_um**2
numero2_ao_quadrado = numero_dois**2

resto = numero_um%2
resto2 = numero_dois%2

soma = numero_um+numero_dois

if numero_um%2 == 0:
    print('O primeiro número é par')
elif numero_um%2 == 1:
    print('O primeiro número é impar')

if numero_dois%2 == 0:
    print('O segundo número é par')
elif numero_dois%2 == 1:
    print('O segundo número é impar') 

if numero_um < 10:
    print('O primeiro número é menor que 10')
elif numero_um == 10:
    print('O primeiro número é igual a 10')
else:
    print('O primeiro número é maior que 10')
if numero_dois < 10:
    print('O segundo número é menor que 10')
elif numero_dois == 10:
    print('O segundo número é igual a 10')
else :
    print('O segundo número é maior que 10')

print("O quadrado do primeiro número é de", numero_ao_quadrado,"e o do segundo número é de" ,numero2_ao_quadrado)

print('O resto da divisao por 2 do primeiro número é de',resto,'e o resto do segundo número é de',resto2)

print('A soma dos dois números é de',soma)


        