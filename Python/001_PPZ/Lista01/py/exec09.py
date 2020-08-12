#Rodrigo Quirino - Python para zumbis
#Lista 01
#Exercício 09
#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
kmtotal = float (input('Digite distância percorrida em quilômetros durante o aluguel: '))
dias = int (input('Digite a quantidade de dias de aluguel: '))
print ('------')
print (f'Distância percorrida: {kmtotal}')
print (f'Dias alugado: {dias}')
print (f'Valor a pagar: {(kmtotal*0.15)+(dias*60)}')
