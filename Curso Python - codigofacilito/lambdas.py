#lamdas
"""
def suma(valor_uno,valor_dos):
    return valor_uno + valor_dos
"""
#funcion equivalente en lambda

mi_funcion = lambda valor_uno, valor_dos : valor_uno + valor_dos
resultado = mi_funcion(3,4)
print(resultado)

formato = lambda sentencia :'¿{}?'.format(sentencia)
no_valor = lambda : 10
no_resultado = lambda : print('Nada')
resultado = formato('Una pregunta')
print(resultado)
print(no_valor())
no_resultado()

