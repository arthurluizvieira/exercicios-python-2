#Classificando categoria dos atletas!

dn = int(input('Digite sua data de nascimento: '))
idade = 2024 - dn
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JÚNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
elif idade > 25:
    print('Categoria MASTER')
print('O atleta tem {} anos!'.format(idade))
