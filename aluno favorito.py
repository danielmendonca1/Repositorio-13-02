while True:
    numero = int(input("Digite um número qualquer para saber se é par ou ímpar: "))

    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")

        continuar = input("Quer verificar outro número? (s/n): ").lower()
    if continuar != 's':
        print("Programa encerrado com sucesso! ")
        break
