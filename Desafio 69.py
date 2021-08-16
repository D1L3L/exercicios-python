limpa = '\033[m'
vermelho = '\033[31m'
verde = '\033[32m'
roxo = '\033[35m'
azul = '\033[34m'
mulhermenor = cont = idade = homens = 0
while True:
    i = int(input(f'{verde}Qual a idade?'))
    if idade > 18:
        idade += 1
    s = ' '
    while s not in 'FM':
        s = input(f'{verde}Qual o sexo[{vermelho}F{verde}/{azul}M{verde}]?').upper().strip()
        if s == 'F' and i < 20:
            mulhermenor += 1
        if s == 'M':
            homens += 1
    cont += 1
    r=' '
    while r not in 'SN':
        r = input(f'{verde}Gostaria de adicionar mais dados[{verde}S{limpa}/{vermelho}N{limpa}]?').upper().strip()
    if r == 'N':
        break
print(f'{roxo}-='*20)
print(f'''{azul}Cadastrados:{verde}{cont}{azul}
Mulheres com menos de 20 anos:{verde}{mulhermenor}
{azul}Homens cadastrados:{verde}{homens}
{azul}Pessoas com mais de 18 anos:{verde}{idade}''')
print(f'{roxo}-='*20)