s = 0
cont = 0
for c in range(1, 500, +2):
    if c%3==0:
        s = s + c
        cont = cont + 1
    print(c)
print('A soma dos {} valores múltiplos de 3 entre 1 e 500, e a soma entre eles é {}.'.format(cont, s))