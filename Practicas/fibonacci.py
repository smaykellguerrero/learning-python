n = int(input("Ingrese la cantidad de terminos que desea obtener :"))
p, s, t = 1, 0, 0
for i in range(0, n):
    s = t
    t = p + s
    p = s
    print(p,end=' ')
