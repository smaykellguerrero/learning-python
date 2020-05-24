def crear_funcion(num_uno,num_dos): # Closure
    def validacion():
        print('Validando')
        return num_uno > 0 and num_dos > 0
    return validacion

def aplicar_funcion(func):
    resultado = func()
    print(resultado)


nueva_funcion = crear_funcion(4,2)
# Algoritmo
aplicar_funcion(nueva_funcion)