valor = float(input('Digite o valor da compra: '))
frase = 'O preço final da sua compra ficou em R$'
forma = int(input("""Digite a forma de pagamento:
1 - Débito/ à vista.
2 - Vencimento.
3 - 2x s/juros.
4 - 3x ou mais.
"""))
if forma == 1:
    preço = valor-(valor*0.1)
    print(frase,'{:.2f}'.format(preço))
elif forma == 2:
    preço = valor-(valor*0.05)
    print(frase,'{:.2f}'.format(preço))
elif forma == 3:
    preço = valor
    parcela= valor/2
    print(frase,'{:.2f} e o valor será parcelado em 2 vezes de R${:.2f}.'.format(preço, parcela))
elif forma == 4:
    parcelas=int(input('Qual o número de parcelas?'))
    preço = (valor+valor*0.2)
    parcela= preço/parcelas
    print(frase,'{:.2f} e o valor será parcelado em {} vezes de R${:.2f}.'.format(preço, parcelas, parcela))