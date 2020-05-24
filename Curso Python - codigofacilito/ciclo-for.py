lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for valor in lista:
    pass

print('\n')


for valor in range(0, 20):
    print(valor)

print('\n')


for valor in range(0, 20, 2):  # con salto
    print(valor)

print('\n')
for indice, valor in enumerate(lista):
    print(valor, "tiene el indice", indice)

print('\n')
for valor in range(0, len(lista)):
    print(valor)

print('\n')
for valor in 'Cúrso de codigo facilito':
    print(valor)

print('\n')
diccionario = {'a': 10, 'b': 20, 'c': 30}
for valor in diccionario:
    print(valor)

print('\n')
for llave, valor in diccionario.items():
    print('llave-> ', valor, ' valor -> ', valor)
