import random
import os
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

def clear():
    os.system('cls')


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
    if a == '':
        a = 1
    if b == '':
        b = 2
    if c == '':
        c = 3
    if d == '':
        d = 4
    if e == '':
        e = 5
    if f == '':
        f = 6
    if g == '':
        g = 7
    if h == '':
        h = 8
    if i == '':
        i = 9
    if a == b and b == c or a == d and d == g or b == e and e == h or c == f and f == i or d == e and e == f or g == h \
            and h == i or a == e and e == i or c == e and e == g:
        return True
    else:
        return False


def decider(flag):
    if flag:
        print('Winner Winner Chicken Dinner')
    else:
        print("It's a DRAW")


def squarer():
    x = int(input('Enter Number: '))
    n = int(input('Enter Power: '))
    answer = x**n
    return answer


def decider_encrypt(text):
    if text == 'a':
        return 1
    elif text == 'b':
        return 2
    elif text == 'c':
        return 3
    elif text == 'd':
        return 4
    elif text == 'e':
        return 5
    elif text == 'f':
        return 6
    elif text == 'g':
        return 7
    elif text == 'h':
        return 8
    elif text == 'i':
        return 9
    elif text == 'j':
        return 10
    elif text == 'k':
        return 11
    elif text == 'l':
        return 12
    elif text == 'm':
        return 13
    elif text == 'n':
        return 14
    elif text == 'o':
        return 15
    elif text == 'p':
        return 16
    elif text == 'q':
        return 17
    elif text == 'r':
        return 18
    elif text == 's':
        return 19
    elif text == 't':
        return 20
    elif text == 'u':
        return 21
    elif text == 'v':
        return 22
    elif text == 'w':
        return 23
    elif text == 'x':
        return 24
    elif text == 'y':
        return 25
    elif text == 'z':
        return 26
    elif text == ' ':
        return 27
    elif text == 'A':
        return 28
    elif text == 'B':
        return 29
    elif text == 'C':
        return 30
    elif text == 'D':
        return 31
    elif text == 'E':
        return 32
    elif text == 'F':
        return 33
    elif text == 'G':
        return 34
    elif text == 'H':
        return 35
    elif text == 'I':
        return 36
    elif text == 'J':
        return 37
    elif text == 'K':
        return 38
    elif text == 'L':
        return 39
    elif text == 'M':
        return 40
    elif text == 'N':
        return 41
    elif text == 'O':
        return 42
    elif text == 'P':
        return 43
    elif text == 'Q':
        return 44
    elif text == 'R':
        return 45
    elif text == 'S':
        return 46
    elif text == 'T':
        return 47
    elif text == 'U':
        return 48
    elif text == 'V':
        return 49
    elif text == 'W':
        return 50
    elif text == 'X':
        return 51
    elif text == 'Y':
        return 52
    elif text == 'Z':
        return 53


def decider_decrypt(text_string):
    if text_string == 1:
        return 'a'
    if text_string == 2:
        return 'b'
    if text_string == 3:
        return 'c'
    elif text_string == 4:
        return 'd'
    elif text_string == 5:
        return 'e'
    elif text_string == 6:
        return 'f'
    elif text_string == 7:
        return 'g'
    elif text_string == 8:
        return 'h'
    elif text_string == 9:
        return 'i'
    elif text_string == 10:
        return 'j'
    elif text_string == 11:
        return 'k'
    elif text_string == 12:
        return 'l'
    elif text_string == 13:
        return 'm'
    elif text_string == 14:
        return 'n'
    elif text_string == 15:
        return 'o'
    elif text_string == 16:
        return 'p'
    elif text_string == 17:
        return 'q'
    elif text_string == 18:
        return 'r'
    elif text_string == 19:
        return 's'
    elif text_string == 20:
        return 't'
    elif text_string == 21:
        return 'u'
    elif text_string == 22:
        return 'v'
    elif text_string == 23:
        return 'w'
    elif text_string == 24:
        return 'x'
    elif text_string == 25:
        return 'y'
    elif text_string == 26:
        return 'z'
    elif text_string == 27:
        return ' '
    elif text_string == 28:
        return 'A'
    elif text_string == 29:
        return 'B'
    elif text_string == 30:
        return 'C'
    elif text_string == 31:
        return 'D'
    elif text_string == 32:
        return 'E'
    elif text_string == 33:
        return 'F'
    elif text_string == 34:
        return 'G'
    elif text_string == 35:
        return 'H'
    elif text_string == 36:
        return 'I'
    elif text_string == 37:
        return 'J'
    elif text_string == 38:
        return 'K'
    elif text_string == 39:
        return 'L'
    elif text_string == 40:
        return 'M'
    elif text_string == 41:
        return 'N'
    elif text_string == 42:
        return 'O'
    elif text_string == 43:
        return 'P'
    elif text_string == 44:
        return 'Q'
    elif text_string == 45:
        return 'R'
    elif text_string == 46:
        return 'S'
    elif text_string == 47:
        return 'T'
    elif text_string == 48:
        return 'U'
    elif text_string == 49:
        return 'V'
    elif text_string == 50:
        return 'W'
    elif text_string == 51:
        return 'X'
    elif text_string == 52:
        return 'Y'
    elif text_string == 53:
        return 'Z'


def decrypter(encrypted_text):
    n = 0
    total = 0
    while True:
        if encrypted_text[n] == 's':
            total += 1
            n += 1
        elif encrypted_text[n] == 'S':
            n += 1
            alphabet = decider_decrypt(total)
            print(alphabet, end='')
            total = 0
        elif encrypted_text[n] == 'X':
            break


def least_sum_array(list1):
    list1.sort()
    list1.reverse()
    list2 = []
    calc = 1000
    length = len(list1)
    x = 0
    y = length - 1
    if not length % 2 == 0:
        calc = length / 2
        calc = calc + 0.1
        calc = calc.__round__()
    length = (length/2)+0.1
    length = length.__round__()
    for iterations in range(length):
        if iterations == (calc - 1):
            num1 = list1[x]
            x += 1
            y -= 1
            list2.append(num1)
        else:
            num1 = list1[x]
            x += 1
            list2.append(num1)
            num2 = list1[y]
            y -= 1
            list2.append(num2)
    list3 = list2[0:2]
    list4 = list2[2:4]
    list5 = list2[4:5]
    list4.reverse()
    list2 = list3 + list5 + list4
    return list2


def dinner_out(string, position, word):
    string = list(string)
    string[position-1] = word
    string = ''.join(string)
    return string


def text_to_symbol(string):
    string = string + ' '
    symbols = {':)': '😄', ':(': '😔', ':|': '😑'}
    for items in range(len(string)):
        for items2 in range(1, len(string) + 1):
            if symbols.__contains__(string[items:items2]):
                simplified_symbol = string[items:items2]
                string = list(string)
                string[items:items2] = symbols.get(simplified_symbol)
                string = ''.join(string)
            if symbols.__contains__(string[items:items2]):
                simplified_symbol = string[items:items2]
                string = list(string)
                string[items:items2] = symbols.get(simplified_symbol)
                string = ''.join(string)
    return string


def factorial(number):
    number = number.__round__()
    if number == 1:
        return 1
    if number < 0:
        if number % 2 == 0:
            number = number * -1
        elif number % 2 == 1:
            number = number * -1
            new_factorial = number * factorial(number - 1)
            return new_factorial * -1
        elif number == -1:
            return 1
    return number * factorial(number - 1)


def student_number_sortout():
    list1 = []
    numbers = 1
    list2 = []
    while not numbers == 0:
        try:
            numbers = int(input('Enter numbers: '))
            if numbers > 520 or numbers < 0:
                raise ValueError
            list1.append(numbers)
        except ValueError:
            print('Please enter a valid value or "0" to END')
    list1.sort()
    list1.reverse()
    length = len(list1) - 1
    for items in range(length):
        if list1[items] == list1[items + 1]:
            list2.append(list1[items])
    for x in list2:
        list1.remove(x)
    list1.remove(0)
    print('')
    count2 = 1
    clear()
    print('Rankings:-')
    for item in range(len(list1)):
        print(f'{count2}th: {list1[item]}        %: {(list1[item]/520)*100}')
        count2 += 1
    count2 = 1
    with open('score.txt', 'a') as f:
        for item in range(len(list1)):
            f.write(f'{count2}th: {list1[item]}        %: {(list1[item]/520)*100}\n')
            count2 += 1
