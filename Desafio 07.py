n= input(Insira o nome do aluno)
n1= float(input('Insira a primeira nota que {} tirou').format(n))
n2=float(input('Insira a segunda nota que {} tirou').format(n))
print ('A media final de {} foi {:.2f}').format(n, float((n1+n2)/2))