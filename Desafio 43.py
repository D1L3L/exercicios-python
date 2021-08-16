peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc=(peso/((altura)**2))

if imc < 18.5:
    print('Com base no seu IMC que é {:.2f} você está abaixo do peso.'.format(imc))
elif imc == 18.5 or imc < 25:
    print('Com base no seu IMC que é {:.2f} você está no peso idea.'.format(imc))
elif imc == 25 or imc < 30:
    print('Com base no seu IMC que é {:.2f} você está com sobre peso.'.format(imc))
elif imc == 30 or imc < 40:
    print('Com base no seu IMC que é {:.2f} você está no estado de obesidade'.format(imc))
elif imc == 40 or imc > 40:
    print('com base no seu IMC que é {:.2f} você está no estado de obesidade morbida'.format(imc))
