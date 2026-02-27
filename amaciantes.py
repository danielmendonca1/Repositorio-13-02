nome1 = input("Nome do primeiro amaciante: ")
valor1 = float(input("Valor do primeiro amaciante: "))
volume1 = float(input("Volume do primeiro amaciante (ml ou L): "))

nome2 = input("Nome do segundo amaciante: ")
valor2 = float(input("Valor do segundo amaciante: "))
volume2 = float(input("Volume do segundo amaciante (ml ou L): "))

if volume1 > volume2:
    print(f"O amaciante {nome1} possui maior volume.")
elif volume2 > volume1:
    print(f"O amaciante {nome2} possui maior volume.")
else:
    print("Os dois amaciantes possuem o mesmo volume.")
