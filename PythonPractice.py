from decimal import Decimal, getcontext
getcontext().prec = 2


def logarithm(number, next_form):
    if number == next_form:
        return 1.0
    elif number < next_form:
        x = Decimal(1.1)
        while True:
            if Decimal(number)**x == next_form:
                return x
            else:
                x = Decimal(x) + Decimal(0.1)


z = Decimal(input(f'log^ '))
y = Decimal(input(': '))
print(logarithm(y, z))
