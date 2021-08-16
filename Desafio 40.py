n=str(input('Digite o nome completo do aluno(a): '))
nome = str(n.title().strip())
primeiro= nome.split()
ano=str(input('Em qual turma o {} está? '.format(primeiro[0])))
n1=float(input('Qual a primeira nota que {} tirou? '.format(primeiro[0])))
n2=float(input('Qual a segunda note que {} tirou? '.format(primeiro[0])))
media=((n1+n2)/2)
if media < 5:
    print('A média de {} da turma {} foi, {:.2f} e infelizmente está REPROVADO!'.format(primeiro[0], ano, media))
elif media == 5:
    print('A média de {} da turma {} foi, {:.2f} e infelizmente ficou em RECUPERAÇÃO!'.format(primeiro[0], ano, media))
elif  5 < media < 7:
    print('A média de {} da turma {} foi, {:.2f} e infelizmente ficou em RECUPERAÇÃO!'.format (primeiro[0], ano, media))
elif media == 7:
    print('A média de {} da turma {} foi {:.2f}, PARABÉNS {} VOCÊ FOI APROVADO!!!'.format (primeiro[0], ano, media, primeiro[0]))
else:
    print('A média de {} da turma {} foi {:.2f}, PARABÉNS {} VOCÊ FOI APROVADO!!!'.format(primeiro[0], ano, media, primeiro[0]))