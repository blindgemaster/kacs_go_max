print('This Program will append Document A and Document B')
while True:
    try:
        doc_name1 = input('Enter the address of Document A: ')
        file_a = open(doc_name1)
        break
    except FileNotFoundError:
        print('The file address is invalid. Try Again')
while True:
    try:
        doc_name2 = input('Enter the address of Document B: ')
        file_b = open(doc_name2)
        break
    except FileNotFoundError:
        print('The file address is invalid. Try Again')
saving_address = input('Enter the address Where You Want to Save : ')
file_write = open(saving_address, 'w')
content = file_a.read() + '\n' + file_b.read()
file_write.write(content)
file_write.close()
file_a.close()
file_b.close()
print('Process Done')
