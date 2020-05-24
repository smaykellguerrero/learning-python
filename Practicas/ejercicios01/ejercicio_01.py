from random import uniform

notas_aprobatorias, notas_desaprobatorias, sumatoria_notas = 0, 0, 0

# llenando array de notas
n = 10
notas = [round(uniform(0, 20), 2) for _ in range(n)]

for nota in notas:
    sumatoria_notas += nota
    if nota > 11.5:
        notas_aprobatorias += 1
    else:
        notas_desaprobatorias += 1
else:
    print('promedio {}'.format(round(sumatoria_notas/n, 2)))
    print('{} {} aprobados'.format(round(100*notas_aprobatorias/n, 2), '%'))
    print('{} {} desaprobados'.format(round(100*notas_desaprobatorias/n, 2), '%'))
