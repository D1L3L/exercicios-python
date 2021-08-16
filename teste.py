import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do próximo aluno: '))
n3 = str(input('Digite o nome do próximo aluno: '))
n4 = str(input('Digite o nome do último aluno: '))
lista = [n1, n2, n3, n4]
aluno = random.choice(lista)
print('O aluno sorteado foi {}.'.format(aluno))