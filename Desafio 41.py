from datetime import date
atual= date.today().year
ano=int(input('Digite o ano de nascimento do atleta: '))
cat= atual-ano
if cat < 9 or cat == 9:
    print('O atleta está na categoria MIRIM.')
elif cat < 14 or cat == 14:
    print('O atleta está na categoria INFANTIL.')
elif cat < 19:
    print('O atleta está na categoria JUVENIL.')
elif cat == 19:
    print('O atleta está na categoria SÊNIOR.')
else:
    print('O atleta está na categoria MASTER.')
