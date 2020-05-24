palabra = str(input("Ingrese palabra a validar->")).lower()

if palabra == palabra[::-1]:
    print("La palabra {} es palindroma".format(palabra))
else:
    print("La palabra {} no es palindroma".format(palabra))
