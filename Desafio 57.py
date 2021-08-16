s = ''
while s != 'M':
    s = str(input('Digite um sexo [M/F]: ').upper().strip())
    if s == 'M':
        print('O sexo é masculino:')
    if s == 'F':
        print('O sexo é feminino:')
        s = 'M'
    if s != 'M':
        print('Tente novamente está resposta não é reconhecida:')

print ('-------FIM-------')
