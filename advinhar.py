import random
numero_secreto = random.randint(1, 10)
palpite = int(input("tente adivinhar o número que eu estou pesando (entre 1 e 10): "))
if palpite == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print("Que pena, o número era", numero_secreto)
                