 #ou também pode ser usado .join() para substituir os espaços. EX.: '---'.join(frase)
frase=str(input('Digite uma palavra ou frase: ')).upper().split()
junto=''.join(frase)
contrario = ''
for letra in range(len(junto) -1, -1, -1):
    contrario += junto[letra]
if contrario == junto:
    print('A frase "{}" é palíndromo da frase "{}".'.format(junto, contrario))
else:
    print('A frase "{}" não é palíndromo da frase "{}".'.format(junto, contrario))