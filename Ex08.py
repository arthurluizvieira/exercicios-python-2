#Analisando Triangulos
s1 = int(input('Digite o primeiro segmento: '))
s2 = int(input('Digite o segundo segmento: '))
s3 = int(input('Digite o terceiro segmento: '))
if s1 == s2 == s3:
    print('Triângulo EQUILATERO!')
elif s1 != s2 != s3 != s1:
    print('Triângulo ESCALENO!')
else:
    print('Triângulo ISÓSCELES!')