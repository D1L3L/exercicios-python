import math
o = float(input('Informe o valor do ângulo: '))
s = math.sin(math.radians(o))
c = math.cos(math.radians(o))
t = math.tan(math.radians(o))
print ('Os valores são: \n  SENO      = {:.2f} \n  COSSENO   = {:.2f} \n  TANGENTE  = {:.2f}'.format(s, c, t))