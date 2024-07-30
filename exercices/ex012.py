preço = float(input('Qual é o preço do produto? Kz'))
novo = preço - (preço * 5 / 100)
print('O produto qu valia {:.2f}Kz, com o desconto de 5% vai custar {:.2f}Kz'.format(preço, novo))
