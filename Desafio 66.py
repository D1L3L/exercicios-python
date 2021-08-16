n = c = 0
branco = '\033[38m'
vermelho = '\033[31m'
verde = '\033[32m'
while True:
    n = int(input(f'Digite valores para somar ou {vermelho}999{branco} para parar:'))
    if n == 999:
        break
    c += n
if c == 0:
    print(f'{verde}O resultado é {vermelho}0{verde}!')
else:
    print(f'A soma dos valores digitados foi {verde}{c:_^2}{branco}!')

