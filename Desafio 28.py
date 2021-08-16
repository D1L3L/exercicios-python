import random
print('Vou pensar em um número entre 0 e 10, tente adivinhar')
computador = random.randint(0, 10)
n = int(input('Qual o número que pensei?'))
if int(n==computador):
    print("Parabéns, o número que imaginei foi {} você adivinhou o que eu pensei".format(computador))
else:
    print('Me parece que você errou,  eu estava pensando no número {}'.format(computador))



