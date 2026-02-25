n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))

op = input("Escolhe (+, -, *, /, **): ")

if op == "+":
    print("Resultado:", n1 + n2)
elif op == "-":
    print("Resultado:", n1 - n2)
elif op == "*":
    print("Resultado:", n1 * n2)
elif op == "/":
    print("Resultado:", n1 / n2 if n2 != 0 else "Não pra dividir o zero obviamente")
elif op == "**":
    print("Resultado:", n1 ** n2)
else:
    print("Operação inválida.")
