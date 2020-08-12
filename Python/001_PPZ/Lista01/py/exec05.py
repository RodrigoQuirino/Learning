#Rodrigo Quirino - Python para zumbis
#Lista 01
#Exercício 05
#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar
preco = float (input('Digite o preço da mercadoria: '))
percdesconto = float (input('Digite o percentual de desconto: '))
print ('------')
print (f'Valor atual do produto: {preco}')
print (f'Percentual do desconto: {percdesconto}')
print (f'Valor do desconto: {preco*(percdesconto/100)}')
print (f'Vaor do produto com desconto: {preco-(preco*(percdesconto/100))} ')
