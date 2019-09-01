import utils

choice = input('Encrypt or Decrypt (e/d): ')
if choice == 'e':
    string = input('Enter Text: ')
    length = len(string)
    print('ET:', end='')
    for items in range(length):
        alpha = string[items]
        multiplier = utils.decider_encrypt(alpha)
        print('s'*multiplier, end='S')
    print('X')
elif choice == 'd':
    code = input('Enter Encrypted Code: ')
    print('DT: ', end='')
    utils.decrypter(code)
else:
    print('Wrong Command!')
print()
print('Made by Khizar')
