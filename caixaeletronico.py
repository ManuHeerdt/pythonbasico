
while True:
    try:
        valor = float(input("Solicite o valor do saque: "))

        if valor <= 0:
          print("O caixa só aceita números positivos!")
        elif valor > 1000:
          print("O caixa não permite saque maior que R$ 1000.")
        else:
            break 

    except ValueError:
         print("Digite apenas números positivos!")

print("Saque realizado:", valor)