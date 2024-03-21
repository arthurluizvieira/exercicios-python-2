#Desafio Aprovando Empréstimo
casa = float(input('Valor da casa: '))
salário = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de {} em {} anos'.format(casa, anos), end=' ')
print('A prestação será de R${}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO')

