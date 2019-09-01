import random


def toss():
    tosser = random.randint(1, 2)
    if tosser == 1:
        print('Player 1 wins the toss')
    else:
        print('Player 2 wins the toss')


def print_table(j, k, l, m, n, o, p, q, r):
    print(f"""
                         |          |
                   {j}     |    {k}     |    {l}
                         |          |
               --------------------------------
                         |          |
                   {m}     |    {n}     |    {o}
                         |          |
               --------------------------------
                         |          |
                   {p}     |    {q}     |    {r}
                         |          |
    """)


def turn_finder(counter):
    if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter == 9:
        symbol = 'o'
    else:
        symbol = '*'
    return symbol


def diagnols(a, b, c, d, e, f, g, h, i):
    if a == b and b == c or a == d and d == g or b == e and e == h or c == f and f == i or d == e and e == f or g == h \
            and h == i or a == e and e == i or c == e and e == g:
        flag = True
    else: flag = False
    return flag


def decider(flag):
    if flag:
        print('Winner Winner Chicken Dinner')
    else:
        print("It's a DRAW")