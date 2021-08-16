from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))

    idade = atual - nascimento
    if idade < 18:
        menor += 1
    else:
        maior += 1
if menor==0:
    print('Nenhuma das sete pessoas citadas é menor de idade.')
elif maior==0:
    print('Nenhuma das sete pessoas citadas é maior de idade.')
else:
    print('{} pessoas citadas são menores de idade e {} são maiores.'.format(menor, maior))



