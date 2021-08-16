v = int(input('Diga a velocidade que o veículo estava: '))
vl = 80
vr = v-vl
multa = 7*vr
if v>vl:
    print('O veículo estava {:.2f}km/h acima do permitido e racebeu uma multa de R${:.2f}.'.format(vr, multa))
else:
    print('O veículo estava dentro da faixa de velocidade permitida.')
