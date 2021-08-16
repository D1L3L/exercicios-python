import random
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do próximo aluno: '))
c = str(input('Digite o nome do próximo aluno: '))
d = str(input('Digite o nome do último aluno: '))
lista = [a, b, c, d]
aluno = random.choice(lista)
print('O aluno selecioado foi {}'. format(aluno))
