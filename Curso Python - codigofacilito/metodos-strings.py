course = 'Curso'
my_string = 'Código Facilito!'

""" Formato """
result = '{a} de {b}'.format(a=course, b=my_string)
result = result.lower() # minuscula
# result = result.upper()  # mayuscula
# result = result.title()  # formato de titulo

""" Busqueda """
pos = result.find('código')
count = result.count('c')

new_string = result.replace('c', 'x')
new_string = result.split(' ')

print(new_string)

