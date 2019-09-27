def input_3_output_largest():
    i = []
    for items in range(3):
        number = input('Please enter a number: ')
        i.append(int(number))
    i.sort()
    print(i[-1])


def three_sample_numbers_sign_product(a, b, c):
    i = [str(a), str(b), str(c)]
    count = 0
    for items in i:
        if '-' in items:
            count += 1
    if count == 1:
        print('-')
    elif count == 2:
        print('+')
    elif count == 3:
        print('-')
    else:
        print('+')


def three_number_sorter(a, b, c):
    i = [a, b, c]
    i.sort()
    i.reverse()
    print(i)


def number_sorter(a, b, c, d, e):
    largest = 0
    for items in range(5):
        if a > largest:
            largest = a
        if b > largest:
            largest = a
        if c > largest:
            largest = c
        if d > largest:
            largest = c
        if e > largest:
            largest = e
    print(largest)


def true_or_odd():
    for items in range(15):
        if (items+1) % 2 == 0:
            print(f'{items+1} is even')
        else:
            print(f'{items+1} is odd')


def fizz_buzz():
    for items in range(100):
        if (items+1) % 3 == 0 and (items+1) % 5 == 0:
            print('bizzfuzz')
        elif (items+1) % 3 == 0:
            print('fizz')
        elif (items+1) % 5 == 0:
            print('buzz')

