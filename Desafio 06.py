n = input('Olá, qual o seu nome?')
v1 = int(input('Que prazer te conhecer {}, agora digite um número!'.format(n)))
print('Com base no valor digitado por você {}, temos que:  \nO dobro de {} é {}. \nO triplo de {} é {}.'
'\nE a raiz quadrada é {}.'.format(n, v1, v1*2, v1, v1*3, int(v1**(1/2))), end=' ')
print ('Obrigado por participar deste desafio! ;)')