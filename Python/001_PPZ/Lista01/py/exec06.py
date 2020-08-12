#Rodrigo Quirino - Python para zumbis
#Lista 01
#Exercício 06
#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem. 
distancia = float (input('Digite a distância a ser percorrida: '))
velocidademedia = float (input('Digite o percentual de desconto: '))
print ('------')
print (f'Distância a percorrer: {distancia}')
print (f'Velocidade média no percurso: {velocidademedia}')
print (f'Tempo total da viagem em horas: {distancia/velocidademedia}')

