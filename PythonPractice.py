e = input('>>>: ')
index = 0
a = ''
number_list = []
for items in range(len(e)):
    if e[items] == '+' or e[items] == '/' or e[items] == '*' or e[items] == '-':
        number_list.append(a)
        number_list.append(e[items])
        a = ''
    else:
        a = a + e[items]
number_list.append(a)
print(number_list)
# for items in range(len(number_list)):
while True:
    if number_list[index] == '/':
        total = float(number_list[index-1])/float(number_list[index+1])
        number_list.pop(index+1)
        number_list.pop(index)
        number_list.pop(index-1)
        number_list.insert(index-1, str(total))
        index = 0
    if '/' not in number_list:
        break
    index += 1
while True:
    if number_list[index] == '*':
        total = float(number_list[index-1])*float(number_list[index+1])
        number_list.pop(index+1)
        number_list.pop(index)
        number_list.pop(index-1)
        number_list.insert(index-1, str(total))
        index = 0
    if '*' not in number_list:
        break
    index += 1
while True:
    if number_list[index] == '+':
        total = float(number_list[index-1])+float(number_list[index+1])
        number_list.pop(index+1)
        number_list.pop(index)
        number_list.pop(index-1)
        number_list.insert(index-1, str(total))
        index = 0
    if '+' not in number_list:
        break
    index += 1
while True:
    if number_list[index] == '-':
        total = float(number_list[index-1])-float(number_list[index+1])
        number_list.pop(index+1)
        number_list.pop(index)
        number_list.pop(index-1)
        number_list.insert(index-1, str(total))
        index = 0
    if '-' not in number_list:
        break
    index += 1
print(number_list)
