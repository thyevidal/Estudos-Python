from random import shuffle

aluno1 = str(input('nome do aluno 1 '))
aluno2 = str(input('nome do aluno 2 '))
aluno3 = str(input('nome do aluno 3 '))
aluno4 = str(input('nome do aluno 4 '))
sorteio = [aluno1, aluno2, aluno3, aluno4]
shuffle(sorteio)

print('A ordem é {}'.format(sorteio))
