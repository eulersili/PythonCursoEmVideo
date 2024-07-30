# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
# do escolhido.

from random import choice
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o trceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

# A diferença entre o "random" e o "choice", é que no "choice" você precisa fazer uma lista em que na qual ele vai sortear. Já no random, você
# apenas precisa de traçar limites, como "de O à 10, escolhe um", ou seja: a = random(0, 10)
