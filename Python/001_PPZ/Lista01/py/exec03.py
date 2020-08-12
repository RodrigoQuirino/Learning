#Rodrigo Quirino - Python para zumbis
#Lista 01
#Exercício 03
#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias = int (input('Digite a quantidade de dias a ser convertido: '))
horas = int (input('Digite a quantidade de horas a ser convertido: '))
minutos = int (input('Digite a quantidade de minutos a ser convertido: '))
segundos = int (input('Digite a quantidade de segundos a ser convertido: '))
print (f'Convesão de dias em segundos: {dias*24*60*60} segundos')
print (f'Convesão de horas em segundos: {horas*60*60} segundos')
print (f'Convesão de minutos em segundos: {minutos*60} segundos')
print (f'Convesão de segundos em segundos: {segundos} segundos')
print ('------')
print (f'Valor total acumulado: {(dias*24*60*60)+(horas*60*60)+(minutos*60)+(segundos)} segundos')

