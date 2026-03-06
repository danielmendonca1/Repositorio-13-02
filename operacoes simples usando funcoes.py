# entrada:
def soma(a,b): return a+b
def subtracao(a,b): return a-b
def multiplicacao(a,b): return a*b
def divisao(a,b): return a/b
def exponencial(a,b): return a**b
# processo/funcao:
while True:
    n1=float(input("digite pra mim o numero 1: "))
    n2=float(input("beleza, agora o numero 2: "))
    op=input("ok, fale uma das operaoes para realizar a açao (+,-,*,/,**):")
    
    if op=="+": print(soma(n1,n2))
    elif op=="-": print(subtracao(n1,n2))
    elif op=="*": print(multiplicacao(n1,n2))
    elif op=="/": print(divisao(n1,n2))
    elif op=="**": print(exponencial(n1,n2))
# saida
    sair=input("deseja continuar?(s/n): ")
    if sair=="n":
     print("sessao encerrada, obrigado...")
    break
