#Rodrigo Quirino - Python para zumbis
#Lista 01
#Exercício 04
#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float (input('Digite o valor atual do salário: '))
percaumento = float (input('Digite o percentual do aumento salarial: '))
print (f'Salário atual: {salario}')
print (f'Percentual do aumento: {percaumento}')
print (f'Valor do aumento: {salario*(percaumento/100)}')
print (f'Valor do novo salário: {salario+(salario*(percaumento/100))} ')
