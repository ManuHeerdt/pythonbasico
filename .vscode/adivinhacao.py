import random
print('*********************************')
print('*******Jogo de Adivinhação*******')
print('*********************************')

print("Escolha o nível de dificuldade:")
print("(1) Fácil - 1 a 10, 10 tentativas")
print("(2) Médio - 1 a 50, 7 tentativas")
print("(3) Difícil - 1 a 100, 5 tentativas")

menu = int(input("Escolha um nível:"))
if(menu == 1):
    total_tentativas = 10
elif (menu == 2):
    total_tentativas = 7
elif (menu == 3):
    total_tentativas = 5

numero_secreto = random.randrange(1,101)






for rodada in range(1, total_tentativas + 1):
    print("Tentativas {} de {}".format(rodada, total_tentativas))

    chute_str = input("Digite seu número: ")
    print("Seu número é: ", chute_str)
    chute = int(chute_str)

    if (chute <1 or chute > 30):
        print("Você tem que digitar um número entre 1 e 30")
        continue

   

    chute = int(chute_str)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou! ")
        break
    else:
        if(maior):
            print("O seu chute foi maior que o número secreto")
        elif(menor):
            print("O seu chute foi menor que o número secreto")
    
print("Fim de jogo!")