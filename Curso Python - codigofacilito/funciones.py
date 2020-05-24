"""

def factorial_numero(numero):
    factorial = 1
    while numero>0:
        factorial = factorial*numero
        numero -=1
    return factorial

print(factorial_numero(5))



def suma(valor_uno, valor_dos, valor_tres):
    return valor_uno + valor_dos + valor_tres

def division(valor_uno,valor_dos):
    return valor_uno / valor_dos

def multiplicacion(valor_uno,valor_dos=10):
    return valor_uno * valor_dos


# Returna tupla
# Diferentes tipos de datos

def multiples_valores():
    return "String",1,False
    
resul = multiples_valores()

cad,ent,bol = multiples_valores()
print(cad)
print(ent)
print(bol)

mi_varianble = multiplicacion
print(mi_varianble(1,2))


print(division(100,10))
print(division(valor_dos=10,valor_uno=100))
print(multiplicacion(12))


def mostrar_resultado(funcion):
    print (funcion(6,8))

mi_varianble = multiplicacion

mostrar_resultado(mi_varianble)


def palindromo(frase):
    # variables locales
    frase = frase.replace(' ','')
    return frase == frase[::-1]

# variables globales
frase = "anita lava la tina"

resul = palindromo(frase)
print(resul)


def variable_global():
    global variable_gloabal
    variable_gloabal = "Adios"

variable_gloabal = "Hola"

print(variable_gloabal)
variable_global()
print(variable_gloabal)



# * -> n valores -> tuplas
# ** -> n valores -> diccionarios
def suma(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(suma(10,20,30))

def sumad(**kwargs):
    valor = kwargs.get('valor','No contiene valor')
    print(valor)

resul= sumad(valor='Eduardo',x=2,y=9,z=True)
print(resul)
"""


