x_axis = []
y_axis = []
x = 0
while True:
    ex_axis = input('Enter X axis: ')
    if ex_axis == 'stop':
        break
    else:
        why_axis = input('Enter Y axis: ')
        x_axis.append(int(ex_axis))
        y_axis.append(int(why_axis))
a = ' '
a1 = ' '
a2 = ' '
a3 = ' '
a4 = ' '
a5 = ' '
b = ' '
b1 = ' '
b2 = ' '
b3 = ' '
b4 = ' '
b5 = ' '
c = ' '
c1 = ' '
c2 = ' '
c3 = ' '
c4 = ' '
c5 = ' '
d = ' '
d1 = ' '
d2 = ' '
d3 = ' '
d4 = ' '
d5 = ' '
e = ' '
e1 = ' '
e2 = ' '
e3 = ' '
e4 = ' '
e5 = ' '
f = ' '
f1 = ' '
f2 = ' '
f3 = ' '
f4 = ' '
f5 = ' '
length = len(x_axis)
for items in range(length):
    if x_axis[x] == 0 and y_axis[x] == 0:
        f = '*'
    elif x_axis[x] == 1 and y_axis[x] == 0:
        f1 = '*'
    elif x_axis[x] == 2 and y_axis[x] == 0:
        f2 = '*'
    elif x_axis[x] == 3 and y_axis[x] == 0:
        f3 = '*'
    elif x_axis[x] == 4 and y_axis[x] == 0:
        f4 = '*'
    elif x_axis[x] == 5 and y_axis[x] == 0:
        f5 = '*'
    elif x_axis[x] == 0 and y_axis[x] == 1:
        e = '*'
    elif x_axis[x] == 1 and y_axis[x] == 1:
        e1 = '*'
    elif x_axis[x] == 2 and y_axis[x] == 1:
        e2 = '*'
    elif x_axis[x] == 3 and y_axis[x] == 1:
        e3 = '*'
    elif x_axis[x] == 4 and y_axis[x] == 1:
        e4 = '*'
    elif x_axis[x] == 5 and y_axis[x] == 1:
        e5 = '*'
    elif x_axis[x] == 0 and y_axis[x] == 2:
        d = '*'
    elif x_axis[x] == 1 and y_axis[x] == 2:
        d1 = '*'
    elif x_axis[x] == 2 and y_axis[x] == 2:
        d2 = '*'
    elif x_axis[x] == 3 and y_axis[x] == 2:
        d3 = '*'
    elif x_axis[x] == 4 and y_axis[x] == 2:
        d4 = '*'
    elif x_axis[x] == 5 and y_axis[x] == 2:
        d5 = '*'
    elif x_axis[x] == 0 and y_axis[x] == 3:
        c = '*'
    elif x_axis[x] == 1 and y_axis[x] == 3:
        c1 = '*'
    elif x_axis[x] == 2 and y_axis[x] == 3:
        c2 = '*'
    elif x_axis[x] == 3 and y_axis[x] == 3:
        c3 = '*'
    elif x_axis[x] == 4 and y_axis[x] == 3:
        c4 = '*'
    elif x_axis[x] == 5 and y_axis[x] == 3:
        c5 = '*'
    elif x_axis[x] == 0 and y_axis[x] == 4:
        b = '*'
    elif x_axis[x] == 1 and y_axis[x] == 4:
        b1 = '*'
    elif x_axis[x] == 2 and y_axis[x] == 4:
        b2 = '*'
    elif x_axis[x] == 3 and y_axis[x] == 4:
        b3 = '*'
    elif x_axis[x] == 4 and y_axis[x] == 4:
        b4 = '*'
    elif x_axis[x] == 5 and y_axis[x] == 4:
        b5 = '*'
    elif x_axis[x] == 0 and y_axis[x] == 5:
        a = '*'
    elif x_axis[x] == 1 and y_axis[x] == 5:
        a1 = '*'
    elif x_axis[x] == 2 and y_axis[x] == 5:
        a2 = '*'
    elif x_axis[x] == 3 and y_axis[x] == 5:
        a3 = '*'
    elif x_axis[x] == 4 and y_axis[x] == 5:
        a4 = '*'
    elif x_axis[x] == 5 and y_axis[x] == 5:
        a5 = '*'
    x += 1
print(f' 5|{a}  {a1}  {a2}  {a3}  {a4}  {a5}')
print(f' 4|{b}  {b1}  {b2}  {b3}  {b4}  {b5}')
print(f' 3|{c}  {c1}  {c2}  {c3}  {c4}  {c5}')
print(f' 2|{d}  {d1}  {d2}  {d3}  {d4}  {d5}')
print(f' 1|{e}  {e1}  {e2}  {e3}  {e4}  {e5}')
print(f' 0|{f}  {f1}  {f2}  {f3}  {f4}  {f5}')
print(f'   ^  ^  ^  ^  ^  ^ ')
print('   0  1  2  3  4  5  ')
input('Enter to continue..')
