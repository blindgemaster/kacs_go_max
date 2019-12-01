from tkinter import *


class Calculator:
    def __init__(self, root):
        self.index = 0
        self.a = []
        root.configure(background='purple')
        root.title('Calculator By Khizar')
        frame0 = Frame(root)
        frame0.pack(side=TOP)
        label1 = Label(frame0, text='Calculator')
        label1.pack(side=TOP)
        frame1 = Frame(root)
        frame1.pack(side=TOP)
        frame3 = Frame(root)
        frame3.pack(side=BOTTOM)
        frame2 = Frame(root)
        frame2.pack(side=BOTTOM)
        frame2.configure(background='purple')
        self.address = Entry(frame1)
        self.address.pack(side=TOP)
        button_1 = Button(frame2, text='1', command=self.inserting1)
        button_1.pack(side=LEFT)
        button_2 = Button(frame2, text='2', command=self.inserting2)
        button_2.pack(side=LEFT)
        button_3 = Button(frame2, text='3', command=self.inserting3)
        button_3.pack(side=LEFT)
        button_4 = Button(frame2, text='4', command=self.inserting4)
        button_4.pack(side=LEFT)
        button_5 = Button(frame2, text='5', command=self.inserting5)
        button_5.pack(side=LEFT)
        button_6 = Button(frame2, text='6', command=self.inserting6)
        button_6.pack(side=LEFT)
        button_7 = Button(frame2, text='7', command=self.inserting7)
        button_7.pack(side=LEFT)
        button_8 = Button(frame2, text='8', command=self.inserting8)
        button_8.pack(side=LEFT)
        button_9 = Button(frame2, text='9', command=self.inserting9)
        button_9.pack(side=LEFT)
        button_0 = Button(frame2, text='0', command=self.inserting0)
        button_0.pack(side=LEFT)
        button_add = Button(frame2, text='+', command=self.inserting_add)
        button_add.pack(side=BOTTOM)
        self.button_equals = Button(frame2, text='=', command=self.equals)
        self.button_equals.pack(side=BOTTOM)
        button_delete = Button(frame2, text='del', command=self.delete)
        button_delete.pack(side=BOTTOM)
        button_quit = Button(frame3, text='quit', command=quit)
        button_quit.pack(side=BOTTOM)
        root.bind('<Return>', self.equals2)

    def equals2(self, a):
        e = self.address.get()
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
        while True:
            if number_list[index] == '/':
                total = float(number_list[index - 1]) / float(number_list[index + 1])
                number_list.pop(index + 1)
                number_list.pop(index)
                number_list.pop(index - 1)
                number_list.insert(index - 1, str(total))
                index = 0
            if '/' not in number_list:
                break
            index += 1
        while True:
            if number_list[index] == '*':
                total = float(number_list[index - 1]) * float(number_list[index + 1])
                number_list.pop(index + 1)
                number_list.pop(index)
                number_list.pop(index - 1)
                number_list.insert(index - 1, str(total))
                index = 0
            if '*' not in number_list:
                break
            index += 1
        while True:
            if number_list[index] == '+':
                total = float(number_list[index - 1]) + float(number_list[index + 1])
                number_list.pop(index + 1)
                number_list.pop(index)
                number_list.pop(index - 1)
                number_list.insert(index - 1, str(total))
                index = 0
            if '+' not in number_list:
                break
            index += 1
        while True:
            if number_list[index] == '-':
                total = float(number_list[index - 1]) - float(number_list[index + 1])
                number_list.pop(index + 1)
                number_list.pop(index)
                number_list.pop(index - 1)
                number_list.insert(index - 1, str(total))
                index = 0
            if '-' not in number_list:
                break
            index += 1
        total = number_list[0]
        self.address.delete(0, END)
        self.address.insert(0, total)

    def inserting1(self):
        self.address.insert(self.index, 1)
        self.index += 1

    def inserting2(self):
        self.address.insert(self.index, 2)
        self.index += 1

    def inserting3(self):
        self.address.insert(self.index, 3)
        self.index += 1

    def inserting4(self):
        self.address.insert(self.index, 4)
        self.index += 1

    def inserting5(self):
        self.address.insert(self.index, 5)
        self.index += 1

    def inserting6(self):
        self.address.insert(self.index, 6)
        self.index += 1

    def inserting7(self):
        self.address.insert(self.index, 7)
        self.index += 1

    def inserting8(self):
        self.address.insert(self.index, 8)
        self.index += 1

    def inserting9(self):
        self.address.insert(self.index, 9)
        self.index += 1

    def inserting0(self):
        self.address.insert(self.index, 0)
        self.index += 1

    def inserting_add(self):
        self.address.insert(self.index, '+')
        self.index += 1

    def equals(self):
        e = self.address.get()
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
        while True:
            if number_list[index] == '/':
                total = float(number_list[index - 1]) / float(number_list[index + 1])
                number_list.pop(index + 1)
                number_list.pop(index)
                number_list.pop(index - 1)
                number_list.insert(index - 1, str(total))
                index = 0
            if '/' not in number_list:
                break
            index += 1
        while True:
            if number_list[index] == '*':
                total = float(number_list[index - 1]) * float(number_list[index + 1])
                number_list.pop(index + 1)
                number_list.pop(index)
                number_list.pop(index - 1)
                number_list.insert(index - 1, str(total))
                index = 0
            if '*' not in number_list:
                break
            index += 1
        while True:
            if number_list[index] == '+':
                total = float(number_list[index - 1]) + float(number_list[index + 1])
                number_list.pop(index + 1)
                number_list.pop(index)
                number_list.pop(index - 1)
                number_list.insert(index - 1, str(total))
                index = 0
            if '+' not in number_list:
                break
            index += 1
        while True:
            if number_list[index] == '-':
                total = float(number_list[index - 1]) - float(number_list[index + 1])
                number_list.pop(index + 1)
                number_list.pop(index)
                number_list.pop(index - 1)
                number_list.insert(index - 1, str(total))
                index = 0
            if '-' not in number_list:
                break
            index += 1
        total = number_list[0]
        self.address.delete(0, END)
        self.address.insert(0, total)

    def delete(self):
        text = self.address.get()
        length = len(text)
        length = length - 1
        text = text[0:length]
        self.address.delete(0, END)
        self.address.insert(0, text)


root1 = Tk()
data_sort = Calculator(root1)
root1.mainloop()
