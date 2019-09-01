import utils


flag = False
a = '1'
b = '2'
c = '3'
d = '4'
e = '5'
f = '6'
g = '7'
h = '8'
i = '9'
symbol = ''
counter = 0
while not flag:
    counter += 1
    symbol = utils.turn_finder(counter)
    utils.print_table(a, b, c, d, e, f, g, h, i)
    cmd = input('>>>')
    if cmd == '1':
        a = symbol
    elif cmd == '2':
        b = symbol
    elif cmd == '3':
        c = symbol
    elif cmd == '4':
        d = symbol
    elif cmd == '5':
        e = symbol
    elif cmd == '6':
        f = symbol
    elif cmd == '7':
        g = symbol
    elif cmd == '8':
        h = symbol
    elif cmd == '9':
        i = symbol
    flag = utils.diagnols(a, b, c, d, e, f, g, h, i)
    if counter == 9:
        break
utils.print_table(a, b, c, d, e, f, g, h, i)
utils.decider(flag)
input('press key to end the program')
