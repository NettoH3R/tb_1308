def calculadora_imc():
    altura = float
    peso = float
    imc = float

    altura = float(input("Digite sua altura em metros: "))
    peso = float(input("Digite seu peso em Kg: ")) 

    imc = round(peso/(altura**2),2)

    print(f"Seu índice de massa corporal(IMC) é de: {imc}")

try:
    calculadora_imc()

except:
    print("\nPor favor digite um numero!")