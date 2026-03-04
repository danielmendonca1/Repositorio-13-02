print("=== Sistema de Cálculo de Tarifa Bancária ===")

tipo_conta = input("bom agr digite o tipo de conta (corrente/poupança): ").lower()
valor = float(input("beleza em seguida digite o valor da movimentação: R$ "))

if tipo_conta == "corrente":
    if valor <= 500:
        tarifa = valor * 0.30
    else:
        tarifa = valor * 0.20

    print(f"tarifa que deve ser paga: R$ {tarifa:.2f}")
elif tipo_conta == "poupanca":
    if valor <- 500:
        tarifa = valor * 0.10
    else:
        tarifa = valor * 0.05

    print(f"Tarifa que deve ser paga: R$ {tarifa:.2f}")
