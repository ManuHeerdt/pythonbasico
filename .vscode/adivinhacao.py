print('*********************************')
print('*******Jogo de Adivinhação*******')
print('*********************************')

numero_secreto = 39

chute_str = input("Digite seu número: ")

print("Seu número é: ", chute_str)

chute = int(chute_str)

if(numero_secreto == chute_str):
    print("Você acertou! ")
else:
    print("Você errou  :( ")