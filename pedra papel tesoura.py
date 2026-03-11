import random

op = ["pedra","papel","tesoura"]
u = p = 0

for i in range(3):
 j = input("pedra, papel ou tesoura?: ").lower()
c = random.choice(op)
print("pc:", c)

if j==c:
    print("oloko, empate para os dois")
elif (j=="pedra" and c=="tesoura") or (j=="papel" and c=="pedra") or (j=="tesoura" and c=="papel"):
    u+=1
    print("você ganhou, parabens")
else:
    p+=1
    print("eita, pc ganhou kkkkkk")
