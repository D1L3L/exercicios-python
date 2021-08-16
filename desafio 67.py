n = 0
r = 0
barra = 'Obrigado por usar este programa!'
while True:
    n = int(input('Quer ver a tabuáda de qual valor? '))
    if 0 > n:
        print('O valor é negativo, o programa será finalizado!')
        break
    else:
        print(f'Tabuáda de {n}:')
        for r in range(1, 11):
            s = r*n
            print(f'{n} x {r} = {s}')
print('=*'*16)
print(f'{barra:^5}')
print('=*'*16)
