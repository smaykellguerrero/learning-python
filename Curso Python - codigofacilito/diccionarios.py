# las claves deben ser inmutables
diccionario = {'a': True, 5: "string", (1, 2): False, 'a': 100, 'a': False}

print(diccionario)

diccionario['c'] = 'string 2'  # creamos clave/valor
print(diccionario)

diccionario['a'] = False  # si la clave se encuentra actualiza si no crea
print(diccionario)

#valor = diccionario[5]
# recoendable usar get al trabajar con diccionarios
valor = diccionario.get('z', False)
print(valor)

del diccionario[5]  # para eliminar con clave
print(diccionario)

llaves = list(diccionario.keys())  # objeto itereble convertir a lista
valores = list(diccionario.values())

print(llaves)

llaves = tuple(diccionario.keys())  # objeto itereble convertir a tupla
valores = tuple(diccionario.values())
print(llaves)

diccionario_dos = {'z': 4, 'w': 9}
# diccionario['z']=diccionario_dos['z'] # no se recomienda
# diccionario['w']=diccionario_dos['w']

diccionario.update(diccionario_dos)
print(diccionario)


