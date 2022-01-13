def area(a,b):
    area = a * b
    print(f'A área de um terreno {a}x{b} é de {area}m².')

print('--' * 15)
print('  CONTROLE DE TERRENOS  ')
print('--' * 15)
a = float(input('LARGURA (m):'))
b = float(input('COMPRIMENTO (m):'))
area(a,b)



