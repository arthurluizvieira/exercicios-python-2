## CALCULADORA DE IMC

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 < IMC < 25:
    print('PESO IDEAL')
elif 25 <= IMC < 30:
    print('SOBREPESO')
elif 30 <= IMC < 40:
    print('OBESIDADE')
elif IMC > 40:
    print('OBESIDADE MÓRBIDA')
print('Seu IMC é de {:2f}'.format(IMC))
