#Exercício de alistamento militar

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    tempo = 18 - idade
    print('Ainda faltam {} anos para o alistamento!'.format(tempo))
    ano = atual + tempo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    tempo = idade - 18
    print('Você já deveria ter se alistado há {} anos!'.format(tempo))
    ano = atual - tempo
    print('Seu alistamento foi em {}.'.format(ano))