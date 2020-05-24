"""
lista = []
for valor in range(0,100):
    lista.append(valor)
"""

#lista = [valor for valor in range(0, 100)]
# Reglas
# 1.- valor a agregar a lista
# 2.-Un cilo for

lista = [valor for valor in range(0, 100) if valor % 2 == 0]
tupla = tuple((valor for valor in range(0, 100) if valor % 2 == 0))
#diccionario = {indice: valor for indice, valor in enumerate(lista)}
diccionario = {indice: valor for indice,valor in enumerate(lista) if indice < 10}
print(diccionario)
