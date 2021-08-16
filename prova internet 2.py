frase = input('Digite seu texto: ').upper().strip().replace(' ','')
letra = input('Agora digite a letra ou número o qual deseja saber quantas vezes ele foi citado:').upper().strip()
if frase.count(letra) > 1:
    print(f'O texto que você digitou contém a string "{letra}" {frase.count(letra)} vezes!')
elif frase.count(letra) == 1:
    print(f'O texto que você digitou contém a string "{letra}" apenas {frase.count(letra)} vez.')
else:
    print(f'O texto que você digitou não contém a string {letra}!')