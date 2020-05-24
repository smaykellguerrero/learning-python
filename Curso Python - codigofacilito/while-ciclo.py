contador = 0

while contador < 10:
    print(contador)
    contador += 1

    if contador == 5:
        print('Estamos en 5')
else:
    print('Fin while')

print('\n')
contador = 0
while contador < 10:
    print(contador)
    contador += 1

    if contador == 5:
        continue

    if contador == 6:
        break
else:
    print('Fin while')

print('\n')
contador = 0
bandera = True
while bandera:
    print(contador)
    contador += 1

    if contador == 5:
        continue

    if contador == 6:
        bandera = False  # break
else:
    print('Fin while')
