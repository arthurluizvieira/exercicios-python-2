#Calcular média de um aluno
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
nt = n1 + n2
m = nt / 2
if m < 5.0:
    print('Você foi REPROVADO!')
elif 7 > m >= 5:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Você foi APROVADO!')
print('Com uma média de {}.'.format(m))