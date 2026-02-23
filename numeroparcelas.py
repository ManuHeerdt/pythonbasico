while True:
    try:
        parcelas = float(input("Escreva o número de parcelas:  "))

        if parcelas >= 12:
          print("O máximo são 12 parcelas")
          continue
        
        else:
            break 

    except ValueError:
         print("Só aceitamos números inteiros")

print("Quantidade de parcelas válida! ", parcelas)