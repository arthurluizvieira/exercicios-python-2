#Desafio calcular valor a ser pago em uma loja com os seguintes desafios:
# à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' Lojas Yokomizo '))
p = float(input('Qual o preço da compra? '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x no cartão''')
opção = int(input('Qual a opção desejada? '))

if opção == 1:
    total = p - (p * 10 / 100) #preço - (10%)

elif opção == 2:
    total = p - (p * 5 / 100) #preço - (5%)

elif opção == 3:
    total = p #total = preço pois nao tem desconto
    parcela = total / 2 #2x no cartao sem juros são duas parcelas
    print('Sua compra será parcelada em 2x de R${}'.format(parcela))

elif opção == 4:
    total = p + (p * 20 / 100) #preço + (20%)
    totalparcelas = int(input('Quantas parcelas? ')) #para escolher quantas parcelas de 3x ou mais
    parcela = total / totalparcelas #parcela = totalparcelas que o usuario digitar
    print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(totalparcelas, parcela))

else:
    total = p
    print('OPÇÃO INVÁLIDA DE PAGAMENTO!')

print('Sua compra de R${:.2f} com o desconto irá ficar em R${:.2f}!'.format(p, total))