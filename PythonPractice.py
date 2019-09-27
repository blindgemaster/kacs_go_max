from tkinter import *


class DataSorter:
    def __init__(self, root):
        frame1 = Frame(root)
        button1 = Button(frame1, text='submit', command=self.answer_giver)
        button1.pack(side=TOP)
        self.my_text_box = Entry(frame1)
        self.my_text_box.pack(side=TOP)

    def answer_giver(self):
        self.my_text_box.insert(0, 'Button Pressed')


root1 = Tk()
ds = DataSorter(root1)
root1.mainloop()
