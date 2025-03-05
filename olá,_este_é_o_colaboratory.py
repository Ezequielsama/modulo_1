

print('Olá mundo!')


a = 3 * 320.52
print(a)

b = 834.47 / 119.21
print(b)

c = 15378.12 / 5
print(c)

cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'

print(f'Olá {cancao.split(' ')[1]}')
print(cancao.swapcase())
print(cancao.title())


noticia = 'Selic vai a 2,75% e supera expectativas; ' + \
'é a primeira alta em 6 anos.'

selic = noticia[12:17]
ano = noticia[62:64]

print(ano)
print(selic)

a = False
b = True

x = not a & b

# not a: Se "a" é Falso, "not a" vira Verdadeiro;
# & b: O operador "&" checa se ambos são Verdadeiros;
# Resultado (Verdadeiro & Verdadeiro): Dá Verdadeiro;
# Assim, "resultado" é Verdadeiro!