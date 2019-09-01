import os


def clear():
    os.system('cls')


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


student_number_sortout()
input()
