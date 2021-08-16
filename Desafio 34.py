frase1 = 'Qual o salário atual do funcionário? '
frase2 = 'O salário do funcionário após o aumento será de R${:.2f}.'
s = float(input(frase1))
if s > float(1250):
    salario = float(s+(s*0.1))
    print(frase2.format(salario))
else:
    salario1 = float(s+(s*0.15))
    print(frase2.format(salario1))
