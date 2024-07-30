larg = float(input('Largura da parede: '))
alt = float(input('Altura da paredee: '))
área = larg * alt
print('Sua parede tem a dimensaão {}x{} e a sua área é de {}m**2'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))

# NOTA: m**2 significa metros ao quadrado.
