while True:
    try:
        quantidade = float(input("Escreva a quantidade de produtos:  "))

        if quantidade <= 0:
          print("Só aceitamos números inteiros e positivos!")
          continue
        
        else:
            break 

    except ValueError:
         print("Não aceitamos letras, apenas números!")

print("Quantidade de produtos:", quantidade)