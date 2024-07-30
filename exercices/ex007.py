n1 = float(input('Nota de Matemática: '))
n2 = float(input('Nota de Química: '))
média = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual {:.1f} Valores.'.format(n1, n2, média))

# NOTA: O {:.1f} diz que ele quer um número decimal depois da vírugula/ponto
# O mesmo para {:.2f}, {:.3f} em diante e ele automaticamente arredonda.
