from random import randint
print('Tente adivinhar em qual número estou pensando:')
v = 0
tentativas =0
rec = ''
n = randint(1, 10)
while v != n:
    v = int(input('Qual é o número? '))
    if v == n:
        print('Acertou!!!')
        tentativas += 1
    else:
        print('Errou!!!')
        tentativas += 1
print('Você acertou na {}° tentativa'.format(tentativas))
print('------------FIM-------------')
