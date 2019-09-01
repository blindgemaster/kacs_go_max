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


listings = [12, 33, 40, 91, 60]
new_list = least_sum_array(listings)
print(new_list)
a, b, c, d, e = new_list
total_sum = (a*b)+(b*c)+(c*d)+(d*e)
print(f'The least total is : {total_sum}')
