#Rodrigo Quirino - Python para zumbis
#Lista 02
#Exercício 01
#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno
lado1 = int (input('Informe o tamanho do primeiro lado: '))
lado2 = int (input('Informe o tamanho do segundo lado: '))
lado3 = int (input('Informe o tamanho do terceiro lado: '))
print('-----')
if lado1 == lado2 and lado1 == lado3:
    print('As medidas informadas são de um triângulo EQUILÁTERO, ou seja, todos os lados são iguais.')
    print(f'Lado A: {lado1} Lado B: {lado2}  Lado C: {lado3} ')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('As medidas informadas são de um triângulo ESCALENO, ou seja, nenhum dos lados é igual.')
    print(f'Lado A: {lado1} Lado B: {lado2}  Lado C: {lado3} ')
else:
    print('As medidas informadas são de um triângulo ISÓSCELES, ou seja, existem dois lados iguais e um diferente')
    print(f'Lado A: {lado1} Lado B: {lado2}  Lado C: {lado3} ')
