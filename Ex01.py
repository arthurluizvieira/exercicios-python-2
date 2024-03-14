nome = str(input('Digite seu nome: '))
if nome == 'Arthur':
    print('Que nome top!!')
elif nome == 'Pedro' or 'Maria' or 'José':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Cláudia, Ana, Jéssica, Viviane, Letícia':
    print('Seu nome é belo feminino.')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!!'.format(nome))
