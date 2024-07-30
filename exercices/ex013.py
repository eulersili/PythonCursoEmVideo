salário = float(input('Qual é o salário do funcionário? Kz'))
novo = salário + (salário * 15 / 100)
print('O funcionário que ganhava {:.2f}Kz, com o aumento de 15% vai ganhar {:.2f}Kz'.format(salário, novo))
