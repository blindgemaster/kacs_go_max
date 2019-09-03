dictionary = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
counter = 1
address = input('Please enter the address without filetype:  ')
with open(f'{address}.out', 'w') as file2:
    with open(f'{address}.in') as file:
        test_counter = int(file.readline())
        while not counter == test_counter+1:
            list1 = []
            dictionary_list = []
            money = 0
            test_number = int(file.readline())
            for items in range(test_number):
                text = file.readline().lower()
                word = text[0]
                list1.append(word)
            for items in range(test_number):
                word2 = list1[items]
                dictionary_list.append(dictionary.get(word2))
            for items in range(test_number):
                for items in range(test_number-1):
                    if dictionary_list[items] > dictionary_list[items+1]:
                        temp = dictionary_list[items]
                        dictionary_list[items] = dictionary_list[items+1]
                        dictionary_list[items+1] = temp
                        money = money + 1
            file2.write(f'case #{counter}: {money}\n')
            counter = counter + 1
