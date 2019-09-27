<<<<<<< HEAD
def input_3_output_largest():
    i = []
    for items in range(3):
        number = input('Please enter a number: ')
        i.append(int(number))
    i.sort()
    print(i[-1])


def three_sample_numbers_sign_product(a, b, c):
    i = [str(a), str(b), str(c)]
    count = 0
    for items in i:
        if '-' in items:
            count += 1
    if count == 1:
        print('-')
    elif count == 2:
        print('+')
    elif count == 3:
        print('-')
    else:
        print('+')
=======
from tkinter import *
import utils


class EncryptDecrypt:
    def __init__(self, root):
        root.title('Encrypt Or Decrypt')
        root.configure(background='blue')
        frame1 = Frame(root)
        frame1.pack(side=TOP)
        frame3 = Frame(root)
        frame3.pack(side=TOP)
        frame2 = Frame(root)
        frame2.pack(side=BOTTOM)
        label1 = Label(frame1, text='Crype')
        label1.pack(side=TOP)
        label3 = Label(frame1, text='Enter Text')
        label3.pack(side=LEFT)
        self.entry1 = Entry(frame1, width=80)
        self.entry1.pack(side=LEFT)
        self.button1 = Button(frame3, text='Encrypt', command=self.encrypt)
        self.button1.pack(side=LEFT)
        self.button3 = Button(frame3, text='Decrypt', command=self.decrypt)
        self.button3.pack(side=LEFT)
        self.button3 = Button(frame3, text='Clear', command=self.clear)
        self.button3.pack(side=LEFT)
        self.quit_button1 = Button(frame2, text='Exit', command=quit)
        self.quit_button1.pack(side=BOTTOM)
        self.entry2 = Text(frame2)
        self.entry2.pack(side=BOTTOM)
>>>>>>> acd2b859413fa9acc01f373b663fd156de7402b4

    def encrypt(self):
        string1 = ''
        text = self.entry1.get()
        length = len(text)
        for items in range(length):
            alpha = text[items]
            multiplier = utils.decider_encrypt(alpha)
            string1 = string1 + ('s' * multiplier) + 'S'
        string1 = string1 + 'X'
        self.entry2.delete(1.0, END)
        self.entry2.insert(END, string1)

<<<<<<< HEAD
def three_number_sorter(a, b, c):
    i = [a, b, c]
    i.sort()
    i.reverse()
    print(i)
=======
    def decrypt(self):
        n = 0
        total = 0
        encrypted_text = self.entry1.get()
        text = ''
        if 'X' in encrypted_text:
            while True:
                if encrypted_text[n] == 's':
                    total += 1
                    n += 1
                elif encrypted_text[n] == 'S':
                    n += 1
                    alphabet = utils.decider_decrypt(total)
                    text = text + alphabet
                    total = 0
                elif encrypted_text[n] == 'X':
                    self.entry2.delete(1.0, END)
                    self.entry2.insert(END, text)
                    break
                else:
                    n += 1
        else:
            self.entry2.delete(1.0, END)
            self.entry2.insert(END, 'ERROR1: "This is not our Decrypted text"')
>>>>>>> acd2b859413fa9acc01f373b663fd156de7402b4

    def clear(self):
        self.entry1.delete(0, END)

<<<<<<< HEAD
def number_sorter(a, b, c, d, e):
    largest = 0
    for items in range(5):
        if a > largest:
            largest = a
        if b > largest:
            largest = a
        if c > largest:
            largest = c
        if d > largest:
            largest = c
        if e > largest:
            largest = e
    print(largest)


def true_or_odd():
    for items in range(15):
        if (items+1) % 2 == 0:
            print(f'{items+1} is even')
        else:
            print(f'{items+1} is odd')


def fizz_buzz():
    for items in range(100):
        if (items+1) % 3 == 0 and (items+1) % 5 == 0:
            print('bizzfuzz')
        elif (items+1) % 3 == 0:
            print('fizz')
        elif (items+1) % 5 == 0:
            print('buzz')

=======

root1 = Tk()
ED = EncryptDecrypt(root1)
root1.mainloop()
>>>>>>> acd2b859413fa9acc01f373b663fd156de7402b4
