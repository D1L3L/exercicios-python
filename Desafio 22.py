nome = str(input('Digite seu nome completo: '))
junto= (nome.replace(' ', ''))
separado= (nome.title().split())

print('Seu nome completo é:', nome.title().strip())
print('Seu nome em caixa alta é: ', nome.upper().strip())
print('Seu nome completo possui ', len(junto), ' letras.')
print(separado[0], 'é seu primeiro nome, e possui ', len(separado[0]), ' letras.')



