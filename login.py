while True:
    try:
        nome = input("Digite seu nome de usuário: ").strip()
        senha = input("Digite sua senha: ").strip()

        if nome =="":
            print("O nome não pode ser vazio. ")
        
        if 0 <= senha <= 10:
            break
        else:
            print("A senha deve ter 6 caracteries.")
    except ValueError:
        print("Digite uma senha válida")

print("Nota registrada!", senha)

print("Nome, nome")