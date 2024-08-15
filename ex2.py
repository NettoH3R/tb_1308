def calcular_viagem():
    consumo = float
    km_da_viagem = float
    total_litros = float


    km_da_viagem = float(input('Digite a distância total da viagem em Km: '))
    consumo = float(input('Digite o consumo do seu carro em KM/L: '))

    total_litros = round(km_da_viagem/consumo,1)

    print(f"Para concluir essa viagem serão necessarios {total_litros} Litros de combustivel")

try:
    calcular_viagem()

except:
    print("Os dados digitados não correspendem aos pedidos")
    