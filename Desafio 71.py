from time import sleep
numero = int(input('Digite um número: '))
outroNumero = int(input('Digite outro valor:'))
operacao = input('Qual a operação gostaria de fazer + ou - ?').split()
resultado = int(0)
if operacao == +:
    resultado = numero + outroNumero
    print(f'A soma dos valores é {resultado}')
elif operacao == -:
    resultado = numero - outroNumero
    print(f'A subtração dos valores é {resultado}')
else:
    print(f'Você digitou {operacao} e este valor não é reconhecido')
    sleep(0.5)
    print('Finalizando')
    sleep(0.5)
sleep(0.5)
print('Fim!')
