ano = int(input('Digite um ano para saber se ele é bissexto: '))
r = int(ano%4)
if r == 0:
    print('O ano digitado é um ano bissexto.')
else:
    print('O ano digitado não é um ano bissexto.')


