my_list = ["Strings", 15, 15.6, True]
print(my_list)

my_list.append(6)  # agregar elemento
print(my_list)

my_list.insert(1, "insert")  # agregar elemento en indice
print(my_list)

# print(my_list[1]) # mostrar segun indice

my_list.remove(15)  # remover elemento
print(my_list)

last_value = my_list.pop()
print(my_list)


my_list_two = [1, 9, 29, 4, 0, 2, 6]
my_list_thre = [22,90]
my_list_two.sort()
print(my_list_two)

my_list_two.sort(reverse=True)
print(my_list_two)

my_list_two.extend(my_list_thre)
print(my_list_two)

my_list_two.append(my_list_thre)
print(my_list_two)