# O mesmo professor do desafio anterior que sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos
# quatro alunos e mosrte a ordem sorteada.

from random import shuffle
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
ordem = shuffle(lista)
print('A ondem de apresentação será {}'.format(lista))

# O "shuffle" serve para "sacudir" uma lista. Ou seja, não pra escolher somente um, mais sim, para escolher aleatoriamente os elementos de um lista
# NOTA: O "shuffle" simplesmente funciona com elementos dentro de parêntes rectos (que representam as listas).
