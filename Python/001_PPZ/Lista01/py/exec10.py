#Rodrigo Quirino - Python para zumbis
#Lista 01
#Exercício 10
#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
totalcigdia = int (input('Digite a quantidade média de cigarros fumados por dia: '))
anos = int (input('Digite a quantidade de anos enquanto fumante: '))
print ('------')
print (f'Cigarros consumidos ao dia: {totalcigdia}')
print (f'Anos fumante: {anos}')
print (f'Média total de cigarros consumidos no período informado:{(totalcigdia*(anos*365))}')
print (f'Redução da vida em dias: {((totalcigdia*(anos*365))*10)/1440}')
