print('huevos y pan')  # comillas simples
print('doesn\'t')  # usa \' para escapar comillas simples...
print("doesn't")  # ...o de lo contrario usa comillas dobles
s = 'Primerea línea.\nSegunda línea.'  # \n significa nueva línea
s  # sin print(), \n es incluído en la salida
print(s)  # con print(), \n produce una nueva línea

print('C:\algun\nombre')  # aquí \n significa nueva línea!

# print(r'C:\algun\nombre')  # nota la r antes de la comilla

print("""\
Uso: algo [OPTIONS]
     -h                        Muestra el mensaje de uso
     -H nombrehost             Nombre del host al cual conectarse
""")
# Las cadenas de texto pueden ser concatenadas (pegadas juntas) con el operador + y repetidas con *:
# 3 veces 'un', seguido de 'ium'
print(3 * 'un' + 'ium')

prefix = 'Py'
prefix + 'thon'
print(prefix)

texto = ('Poné muchas cadenas dentro de paréntesis '
         'para que ellas sean unidas juntas.')

print(texto)


# Las cadenas de texto se pueden indexar (subíndices), el primer carácter de la cadena tiene el índice 0. No hay un tipo de dato para los caracteres; un carácter es simplemente una cadena de longitud uno:
palabra = 'Python'
print(palabra[0])  # caracter en la posición 0
print(palabra[5])  # caracter en la posición 5
print(palabra[-1])  # último caracter
print(palabra[-2])  # ante último caracter

# Nota que -0 es lo mismo que 0, los índice negativos comienzan desde -1

# caracteres desde la posición 0 (incluída) hasta la 2 (excluída)
print(palabra[0:2])

# caracteres desde la posición 2 (incluída) hasta la 5 (excluída)
print(palabra[2:5])

# Nota como el primero es siempre incluído, y que el último es siempre excluído. Esto asegura que s[:i] + s[i:] siempre sea igual a s:
print(palabra[:2] + palabra[2:])
print(palabra[:4] + palabra[4:])

# Los índices de las rebanadas tienen valores por defecto útiles; el valor por defecto para el primer índice es cero, el valor por defecto para el segundo índice es la longitud de la cadena a rebanar.
# caracteres desde el principio hasta la posición 2 (excluída)
print(palabra[:2])

# caracterrs desde la posición 4 (incluída) hasta el final
print(palabra[4:])

# caracteres desde la ante-última (incluída) hasta el final
print(palabra[-2:])

# Las cadenas de Python no pueden ser modificadas -- son immutable. Por eso, asignar a una posición indexada de la cadena resulta en un error:
# palabra[0] = 'J'

# Si necesitás una cadena diferente, deberías crear una nueva:

print('J' + palabra[1:])
print(palabra[:2] + 'py')

s = 'supercalifrastilisticoespialidoso'
print(len(s))
