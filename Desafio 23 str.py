valor = int(input('Digite um valor inteiro entre 0 e 99999: '))
u = ((valor//1))
d = valor // 10
c = valor // 100
m = valor // 1000
print('A unidade do valor digitado é:  ', u [::4] )
print('A dezena do valor digitado é:   {}'.format(d))
print('A centena do valor digitado é:  {}'.format(c))
print('O milhar do valor digitado é:   {}'.format(m))