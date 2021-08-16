p = float( input('Digite o preço do produto: '))
pf = float( p-(p*0.05))
print('O valor do produto com o desconto de 5% ficou em R${:.2f} e você obteve um desconto de R${:.2f}'.format(pf, (p-pf)))

#Este exercício tem objetivo de adicionar um desconto de 5% ao preço de um produto e mostra qual o total em desconto obtido