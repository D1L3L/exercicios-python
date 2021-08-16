valor = ('zero','um','dois','três', 'quatro', 'cinco', 'seis', 'sete\n'
,'oito','nove','dez','onze', 'doze','treze', 'quatorze', 'quinze', 'dezesseis\n'
, 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número valor entre 0 e 20: '))
    if 0 <= numero >= 20:
        print('Ops, ', end='')
    elif numero in range(0,21):
        print(f'O número digitado foi {valor[numero]}.')
        break
    print(f'{numero} não está entre 0 e 20.')
print('-=-'*12)