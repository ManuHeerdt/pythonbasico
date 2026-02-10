while True:
    try:
        idade = int(input("Digite sua idade "))
        if idade <= 0:
            print("A idade não aceita zero e números negativos.")
        else:
            break
    except ValueError:
        print("Idade inválida! Digite apenas números.")

print("Idade Cadrastada: ", idade)

