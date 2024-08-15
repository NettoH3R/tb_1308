def tabuada():

    numero = int
    mult = int


    numero = int(input("Digite o número para calcular a tabuada: "))

    for count in range(1,11):

        mult = numero * count
            
        print(f"{numero} x {count} = {mult}")


try:
    tabuada()
except:
    print("\nPor favor digite um numero!")