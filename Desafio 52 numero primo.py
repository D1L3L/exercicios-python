n = int(input('Digite um número: '))
total = 0
for p in range(1, n+1):
    if n % p==0:
        print('\033[36m', end=' ')
        total += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(p), end='')
print('\n O número {} foi dividido {} vezes.'.format(n, total))
if total>2:
    print(' O numero {} não é um número primo!'.format(n))
else:
    print(' O número {} é um número primo!'.format(n))





