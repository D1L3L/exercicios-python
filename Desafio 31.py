d = float(input('Para saber o preço da passagem, digite a distância em km: '))
if d>200:
   valor = float(d*0.45)
   print('O preço da sua passagem é R${:.2f}.'.format(valor))
else:
    preco = float(d*0.50)
    print('O preço da sua passagem é R${:.2f}.'.format(preco))