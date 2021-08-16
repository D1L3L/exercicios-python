vel = float(input('Qual a velocidade do veículo?'))
lim = float(80)
crime = float(vel-lim)
multa = float(7*crime)
if vel>lim:
    print('O veículo estava {:.2f}km/h acima da velocidade permitida e vai receber uma multa no valor de R${:.2f}.'.format(crime, multa))

print('---FIM---')

