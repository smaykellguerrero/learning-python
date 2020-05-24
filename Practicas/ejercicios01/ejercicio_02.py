from random import randint
n = 10
numbers = [round(randint(100, 700), 2) for _ in range(n)]
print(numbers)
print('el número menor es {}'.format(min(numbers)))
