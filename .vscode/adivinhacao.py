import random
print('*********************************')
print('*******Jogo de Adivinhação*******')
print('*********************************')

numero_secreto = random.randrange(1,101)
total_tentativas = 10
rodada = 1



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