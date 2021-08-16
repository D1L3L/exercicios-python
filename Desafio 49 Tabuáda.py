from time import sleep
n = int(input('Qual o valor que você gostaria de saber a tabuáda?'))
l = int(input('Até qual multiplicador quer a tabuáda?'))
v = int(1)
for t in range (1, l+1):
    v = n*t
    print('{} x {} = {}'.format(n, t, v))
    sleep(0.25)
sleep(0.5)
print('''
      FIM!!!''')
