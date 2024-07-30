print('----------Gerador de PA----------')
print('-=-' * 11)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro # Por que o primeiro "termo" é o "primeiro"
cont = 1
while cont <= 10:
    print(f'{termo} -', end=' ')
    termo += razao
    cont += 1
print('FIM')
