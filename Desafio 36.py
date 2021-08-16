renda=float(input('Informe a sua renda mensal: '))
parcela=float(renda/3)
valor=float(input('Informe o valor do imóvel: '))
tempo=int(input('Em quantos anos pretende pagar o imóvel?'))
meses=float(tempo*12)
parcelareal=valor/meses
if parcelareal>parcela:
    print('O seu financiamento não foi autorizado, tente novamente em breve.')
else:
    print('Parabéns o seu financiamento foi aprovado, e sua parcela ficou estimada em: {:.0f} vezes de R${:.2f} '.format(meses, parcelareal))


