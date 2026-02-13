while True:
    try:
        nome = input("Solicite o valor do saque: ")
        
        if nome >= 0:
            print("O caixa só aceita números positivos!.")
        else:
            break
    except ValueError:
        print("O caixa não permite saque maior que R$ 1000.")

print("Saque Realizado: ", nome)