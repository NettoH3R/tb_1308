def calcular_media():

    notas= []
    nota_entrada = float

    soma = float
    media =float

    count = 1

    while count <= 6:

        nota_entrada = float(input(f"Digite a {count}ª nota: "))

        if nota_entrada >= 0 and nota_entrada <= 10:   

            notas.append(nota_entrada)
            count += 1

        else:
            print("A nota deve ter um valor entre 0 e 10\n\n")
        


        soma = sum(notas)

        media = (soma/len(notas))

    if media < 4.5:
        print("\nAluno está reprovado :(")

    elif 4.5 <= media <=6:
        print("\nO aluno terá que fazer uma sub '-'")
        
    else:
        print("\nAluno aprovado!")



try:
    calcular_media()

except:
    print("\nPor favor digite um numero!")
