while True:
    try:
        ano= float(input("Escreva seu ano de nascimento  "))

        if ano <= 1900:
          print("O ano deve ser maior que 1900")
        elif ano >= 2026:
          print("O ano deve ser menor que 2026")
          continue
        
        else:
            break 

    except ValueError:
         print("Não aceitamos letras, apenas números!")

print("Ano de nascimento válido", ano)