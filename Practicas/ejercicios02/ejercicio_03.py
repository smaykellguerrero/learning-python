from numpy import array

cartilla = array([
    [4, 1, 5, 6, 3, 8, 9, 7, 2],
    [3, 6, 2, 4, 7, 9, 1, 8, 5],
    [7, 8, 9, 2, 1, 5, 3, 6, 4],
    [9, 2, 6, 3, 4, 1, 7, 5, 8],
    [1, 3, 8, 7, 5, 6, 4, 2, 9],
    [5, 7, 4, 9, 8, 2, 6, 3, 1],
    [2, 5, 7, 1, 6, 4, 8, 9, 3],
    [8, 4, 3, 5, 9, 7, 2, 1, 6],
    [6, 9, 1, 8, 2, 3, 5, 4, 7],
])


def validar_fila(n):
    global cartilla
    es_valida = True
    fila_n = cartilla[n, :].tolist()
    for i in range(9):
        apariciones = fila_n.count(i+1)
        if apariciones != 1:
            es_valida = False
            break
    return es_valida


def validar_columna(n):
    global cartilla
    es_valida = True
    columna_n = cartilla[:, n].tolist()
    for i in range(9):
        apariciones = columna_n.count(i+1)
        if apariciones != 1:
            es_valida = False
            break
    return es_valida


def validar_region(n):
    global cartilla
    es_valida = True
    if n < 3:
        a, b = 0, 3
        c, d = (n*3), ((n+1)*3)
    elif n < 6:
        n -= 3
        a, b = 3, 6
        c, d = (n*3), ((n+1)*3)
    else:
        n -= 6
        a, b = 6, 9
        c, d = (n*3), ((n+1)*3)

    region_n = cartilla[a:b, c:d].tolist()
    region_n = region_n[0]+region_n[1]+region_n[2]
    for i in range(9):
        apariciones = region_n.count(i+1)
        if apariciones != 1:
            es_valida = False
            break
    return es_valida


def validar_soduko():

    for i in range(9):
        es_valida = validar_fila(i)
        print('{0:8} : {1:1} ==> {2:5}'.format('Fila', i, str(es_valida)))
        if not es_valida:
            return False

    for i in range(9):
        es_valida = validar_columna(i)
        print('{0:8} : {1:1} ==> {2:5}'.format('Columna', i, str(es_valida)))
        if not es_valida:
            return False

    for i in range(9):
        es_valida = validar_region(i)
        print('{0:8} : {1:1} ==> {2:5}'.format('Region', i, str(es_valida)))
        if not es_valida:
            return False

    return True


print('Soduko es valido: {}'.format(validar_soduko()))
