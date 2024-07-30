import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, raiz))

print('A raiz quadrada de {} é igual a {}'.format(num, math.ceil(raiz)))
# O "ceil" obriga o número a ser arredondado para cima mesmo que não está na posição para tal.

print('A raiz quadrada de {} é igual a {}'.format(num, math.floor(raiz)))
# O "floor" obriga o número a ser arredondado para baixo mesmo que não está na posição para tal.

print('A raiz quadrada de {} é igual a {:.4f}'.format(num, (raiz)))
# O "{:.2f} ou outro número diferente de 2" obriga a ser um número decimal e arredonda para cima se possível.

# Ou podemos importar somente o essencial (o que queremos) de cada biblioteca:

from math import sqrt, floor
num  = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, floor(raiz)))

# Outro exemplo:

from math import factorial
n = int(input('Digite um valo:  '))
print('O número {}, tem com factorial {}'.format(n, factorial(n)))