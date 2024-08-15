def caixa_eletronico():

    valor = int

    notas = [200, 100, 10, 5, 1]

    
    valor = int(input("Digite o valor que deseja sacar (entre 10 e 1500 reais): "))
    

    if valor < 10 or valor > 1500:
        print("Valor inválido. O valor deve estar entre 10 e 1500 reais.")
        return
    

    print("\nNotas fornecidas:")
    for nota in notas:
        quantidade = valor // nota
        valor = valor % nota
        if quantidade > 0:
            print(f"{quantidade} nota(s) de R$ {nota}")
    
    if valor > 0:
        print(f"Sobrou um valor de R$ {valor} que não pode ser sacado com as notas disponíveis.")


try:
    caixa_eletronico()

except:
    print("\nPor favor digite um numero!")