print('[B|O] [X|K] [D|Q] [C|P] [N|A] [G|T] [R|E] [T|G] [Q|D] [F|S]')
print('[J|W] [H|U] [V|I] [A|N] [O|B] [E|R] [F|S] [L|Y] [P|C] [Z|M] ')
print('                           THE BLOCK GAME!')
print('')
search_string = input('Enter Your Word: ')
search_string = search_string.lower()
search_string = ' ' + search_string + ' '
length = len(search_string)
found = False
found1 = False
with open('new_file.txt', 'r') as file:
    for items in range(20):
        word = file.readline()
        word1 = word[0]
        word2 = word[1]
        found1 = False
        for items2 in range(length):
            if word1 == search_string[items2] and not found1:
                if search_string[items2+1] == word2:
                    search_string = list(search_string)
                    search_string[items2] = '*'
                    search_string[items2+1] = '*'
                    search_string = ''.join(search_string)
                    found1 = True
                elif search_string[items2 - 1] == word2:
                    search_string = list(search_string)
                    search_string[items2] = '*'
                    search_string[items2 - 1] = '*'
                    search_string = ''.join(search_string)
                    found1 = True
length = length - 2
end_word = ' ' + ('*'*length) + ' '
if search_string == end_word:
    found = True
if found:
    print('                        Winner Winner Chicken Dinner!')
else:
    print('                              You Lost!')
