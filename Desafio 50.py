from time import sleep
s = 0
for c in range(1, 7):
    n = int(input("Digite um número:"))
    d = n%2
    if d != 0:
        n = 0
    else:
        n = n
    s = s + n
print('Calculando...')
sleep(0.25)
print('A soma dos números pares é {}!'.format(s))
sleep(1)
print('Fim!')