while True:
    peso = float(input("Digite o peso de Lucas (kg): "))

    agua_ml = peso * 15
    copos = agua_ml // 250

    print("Lucas deve beber", int(copos), "copos de água por dia.")

    repetir = input("Deseja calcular novamente? (s/n): ")
    if repetir.lower() != "s":
        print("Programa encerrado.")
        break
        
