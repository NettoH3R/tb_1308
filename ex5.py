def calcular_iptu():
    
    iptu = float

    lagura = float
    comprimento = float

    m_quad = float

    print("Digite as dimensões do seu imóvel em m\n")  

    lagura = float(input("Largura: "))
    comprimento = float(input("Comprimento: "))

    iptu = ((lagura*comprimento)* 8.14)

    print(f"O IPTU será R$ {iptu} para esse imóvel imformado")

try: 
    calcular_iptu()

except:    
    print("\nPor favor digite um numero!")