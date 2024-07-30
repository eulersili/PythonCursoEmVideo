from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
# Podemos colocar o "trunc" dentro do format no print, ou antes do "float" na variável, como: num = trunc(float(input('Digite um número: ')))
