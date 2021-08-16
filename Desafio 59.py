botao=0
rec=0
rep= ''
while botao != 5:
    rec += 1
    n1 = int(input('Digite um número:'))
    n2 = int(input("Digite outro número: "))
    botao = int(input('''Digite um valor para selecionar:
    [1]Somar:
    [2]Multiplicar:
    [3]Maior:
    [4]Novos números:
    [5]Sair do programa:
    '''))
    if botao == 1:
        soma = n1+n2
        print('O resultado é: {}+{}={}'.format(n1, n2, soma))
        rep =''
        while rep != 'S':
            rep = str(input('Gostaria de realizar outra operação?[S/N]').upper())
            if rep == 'N':
                botao = 5
                rep = 'S'
                rec += 1
            if rep == 'S':
             rep = 'S'
    if botao == 2:
        multiplicar= n1*n2
        print('O resultado é: {}x{}={}'.format(n1, n2, multiplicar))
        while rep != 'S':
            rep = str(input('Gostaria de realizar outra operação?[S/N]').upper())
            if rep == 'N':
                botao = 5
                rep = 'S'
                rec += 1
            if rep == 'S':
                rep = 'S'
    if botao == 3:
        if n1>n2:
            print('{} é maior que {}.'.format(n1, n2))
        elif n1 == n2:
            print('{} é igual à {}.'.format(n1, n2))
        elif n1<n2:
            print('{} é maior que {}.'.format(n2, n1))
        while rep != 'S':
            rep = str(input('Gostaria de realizar outra operação?[S/N]').upper())
            if rep == 'N':
                    botao = 5
                    rep = 'S'
                    rec += 1
            if rep == 'S':
                    rep = 'S'
    if botao == 4:
        rec -= 1
    if botao == 5:
        rec -=1
if rec == 1:
    print('Você utilizou o programa apenas uma vez.')
elif rec == 0:
    print('Que pena, você não utilizou o programa.')
else:
    print('Você utilizou o programa {} vezes.'.format(rec))
print('------------------Fim--------------------')