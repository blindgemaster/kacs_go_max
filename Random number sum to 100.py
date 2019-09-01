from random import randint
total = 0
x = 100
the_list = []
while True:
    if total == 100:
        break
    if x == 0:
        break
    sign = randint(1, 2)
    if sign == 1:
        number = randint(1, x)
        x = x - number
        total = total + number
        the_list.append(f'+ {number}')
    elif sign == 2:
        number = randint(1, x)
        x = x + number
        total = total - number
        the_list.append(f'- {number}')

print(the_list)
