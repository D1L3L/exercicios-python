from random import randint
fim = cont = 0
ciano = '\033[36m'
vermelho = '\033[31m'
while True:
    valor = int(input('Digite um valor: '))
    jogada = (input('Você vai apostar em par ou ímpar?[P/I]').upper())
    if jogada == 'P':
        fim = 0
    if jogada == 'I':
        fim = 1
    n = randint(0,10)
    soma = valor + n
    resultado = soma % 2
    if resultado == fim:
        cont +=1
    elif resultado != fim:
        break
print(f'{ciano}=-'*20)
print(f'{vermelho}Fim de jogo, você ganhou {cont} tentativas.')
print(f'{ciano}=-'*20)
