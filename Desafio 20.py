import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do próximo aluno: ')
n3 = input('Digite o nome do próximo aluno: ')
n4 = input('Digite o nome do pr[oximo aluno: ')
lista = [n1, n2, n3, n4]
sequencia = random.shuffle(lista)
print('A sequência escolhida é:')
print(lista)
