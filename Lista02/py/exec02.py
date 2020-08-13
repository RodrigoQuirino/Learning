#Rodrigo Quirino - Python para zumbis
#Lista 02
#Exercício 02
#Determine se um ano é bissexto. Verifique no Google como fazer isso...
#Para ser bissexto, o ano deve ser:
# - Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
# - Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
# - Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.
ano = int (input('Informe um ano para determinar se ele é bissexto ou não: '))

print('-----')
if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    print(f'O ano {ano} É bissexto')
else:
    print(f'O ano {ano} NÃO É bissexto')
