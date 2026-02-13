while True:
    try:
        nome = input("Digite seu nome de usuário: ").strip()
        senha = input("Digite sua senha, ela deve ter 6 caracteries: ")

        if nome =="":
                print("O nome não pode ser vazio. ")
                continue
        if len(senha) <= 6:
               break
        else:
             print("A senha deve ter 6 caracteries.", senha )

    except ValueError:
        print("Digite uma senha válida")

        
  
print("Login cadastrado com sucesso!", senha)

print("Nome", nome)