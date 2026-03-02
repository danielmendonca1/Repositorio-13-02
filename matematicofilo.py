while True:
    print("\n=== verificador de Triângulos sla ===")

    a = float(input("so digite o primeiro lado da reta: "))
    b = float(input("so digite o segundo lado da reta: "))
    c = float(input("so digite o terceiro lado da reta: "))

        # Verificacao se forma triângulo de fato:
    if a + b > c and a + c > b and b + c > a:
        print("Forma um triângulo!")

        # Verificacao do tipo de triangulo:
        if a == b == c:
            print("Triângulo Equilátero")
        elif a == b or a == c or b == c:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
    else:
        print("Não forma um triângulo obviamente")

    continuar = input("\nQuer tentar verificar outro triangulo?? (s/n): ").lower()
    if continuar != "s":
        print("Programa encerrado com sucesso obrigado")
        break
