numero = int(input())
outroNumero = int(input())
operacao = ''
r = 0
while True:
    operacao = input()
    if operacao == '-':
        r = numero - outroNumero
        print (f'{r}')
        break
    if operacao == '+':
        r = numero + outroNumero
        print (f'{r}')
        break
    else:
        print(f'{r}')
        break

#############################################

n = int(input().strip())
r = 0
for r in range(0, n):
    r+= n
print(r)

#############################################