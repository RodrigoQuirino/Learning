velocidade = int(input("Qual é a velocidade atual de seu veículo? "))
if velocidade <= 110:
    print("Seu veículo está na velocidade permitida")
else:
    print(f"Você acaba de ser multado. O valor total de sua multa é R$ {(velocidade-110)*5:.2f}")
