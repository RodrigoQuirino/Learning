utilizacao = int (input('Informe o tempo de utilização dos serviços telefônicos em minutos: '))
if utilizacao < 200:
    print(f'O valor da sua conta devido utilização de {utilizacao} minutos é: {utilizacao*0.2:.2f}')
elif utilizacao >= 200 and utilizacao <= 400:
    print(f'O valor da sua conta devido utilização de {utilizacao} minutos é: {utilizacao*0.18:.2f}')
elif utilizacao <= 800:
    print(f'O valor da sua conta devido utilização de {utilizacao} minutos é: {utilizacao*0.15:.2f}')
else:
    print(f'O valor da sua conta devido utilização de {utilizacao} minutos é: {utilizacao*0.08:.2f}')
        
