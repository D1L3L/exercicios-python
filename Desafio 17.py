from math import hypot
cato = float(input('Digite o valor do cateto oposto'))
cata = float(input('Digite o valor do cateto adjacente'))
hip = hypot(cata, cato)
print("O valor da hipotenusa é {:.2f}".format(hip))

#Este exercício tem a finalidade de criar um programa que calcule a hipotenusa a partir das coordenadas usando módulo