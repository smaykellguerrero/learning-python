def decorador(func):# A, B
    def nueva_funcion():
        # Agrege codigo
        print('Vamos a ejecuta la función')
        func()
        # Agrege codigo
        print('Funcion fue ejecutada')
    return nueva_funcion #  C

@decorador
def saluda():
    print('Hola')

@decorador
def suma():
    print(10 + 20)

suma()
# A, B, C son funciones
# A recibe como parametro B para poder crear C