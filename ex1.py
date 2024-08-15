def calcular_idade():
    idade = int

    idade = int(input("digite sua Idade: "))

    if 0 <= idade < 11 :
        print("Classificação criança")

    elif 11 <= idade <=13:
        print("Classificação pré-adolecente")

    elif 13 < idade < 18:
        print('Classificação adolecente')

    elif 18 <= idade < 150:
        print('Classificação adulto')
    else:
        print('O valor digitado é invalido')

try: 
    calcular_idade()

except:
    print('Espera-se que o valor digitado seja um numero entre 0 a 150')
    