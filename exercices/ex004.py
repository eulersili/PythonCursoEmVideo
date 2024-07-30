a = input('Digite algo: ')
print('Só tem espaço?', a.isspace())

print('O tipo primitivo deste valor é', type(a))
# O tipo primitivo (type) de todos os valores que entrarem (se, se mantiver apenas "input()..."), serão sempre "<class 'str'>", o que significa
# que é uma string, pois, no "input" não definimos se é "int", "float" ou outra coisa.

print('É alfabético?', a.isalpha())
print('É um número?', a.isnumeric())
print('Está em minúsculo?', a.islower())
print('Está em maiúsculo?', a.isupper())
print('Está capitalizada?', a.istitle())
