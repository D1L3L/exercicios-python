#qual a média de idade do grupo?
media=0
soma=0
#qual o nome do homem mais velho do grupo?
idade=0
nomevelho=''
#quantas mulheres têm menos de 20 anos?
menor=0
mulhernova=0
for dados in range(1,5):
    print('---------------------------------------------')
    n = str(input('Digite o nome da {}° pessoa: '.format(dados))).title().strip()
    i = int(input('Qual a idade desta pessoa? '))
    s = str(input('Qual o sexo desta pessoa[F/M]? ')).title().strip()
    print('Confira: {}, {} anos e é do sexo {}.'.format(n, i, s))
    soma += i
    if i!=0:
        media = (soma)/4
    if s in 'F' and i < 20:
        menor += 1
    if dados == 1 and s in 'M':
        nomevelho = n
        idade = i
    elif i > idade and s in 'M':
        nomevelho = n
        idade = i

print('a média das idades é {:.2f} anos.'.format(media))
if menor == 0:
    print('Não foi citado nenhuma mulher abaixo de 20 anos.')
elif menor == 1:
    print ('Apenas uma mulher tem idade abaixo de 20 anos.')
elif menor > 1:
    print('{} mulheres tem menos de 20 anos.'.format(menor))
if idade != 0:
    print('O homem mais velho é {} e ele tem {} anos.'.format( nomevelho, idade))
else:
    print('Não foi colocado nenhum dado masculino.')

