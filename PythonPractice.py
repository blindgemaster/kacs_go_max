import utils
from tkinter import *
from random import randint


class TicTacToe:
    def __init__(self, root):
        root.resizable(0, 0)
        root.configure(background='blue')
        self.list1 = [0, 2, 4, 6, 8]
        self.list2 = [1, 3, 5, 7, 9]
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.d = StringVar()
        self.e = StringVar()
        self.f = StringVar()
        self.g = StringVar()
        self.h = StringVar()
        self.i = StringVar()
        self.label_define = StringVar(value='Please initialise')
        self.counter = 0
        self.flag = False
        self.a1flag = True
        self.b1flag = True
        self.c1flag = True
        self.d1flag = True
        self.e1flag = True
        self.f1flag = True
        self.g1flag = True
        self.h1flag = True
        self.i1flag = True
        root.title('Brit by Khizar')
        root.geometry('300x500')
        frame1 = Frame(root)
        frame1.pack()
        label_welcome = Label(frame1, text='Welcome to Brit')
        label_welcome.config(font=('Courier', 18, 'bold'))
        label_welcome.pack()
        frame2 = Frame(root)
        frame2.pack(side=TOP)
        frame4 = Frame(root)
        frame4.pack(side=BOTTOM)
        frame3 = Frame(root)
        frame3.pack(side=BOTTOM)
        end_label = Label(frame3, textvariable=self.label_define)
        end_label.config(font=('Courier', 12, 'bold'))
        end_label.pack(side=LEFT)
        canvas = Canvas(frame2)
        canvas.create_line(20, 100, 280, 100)
        canvas.create_line(20, 175, 280, 175)
        canvas.create_line(100, 30, 100, 250)
        canvas.create_line(200, 30, 200, 250)
        canvas.pack()
        label1 = Label(frame2, textvariable=self.a)
        label1.config(font=('Courier', 44))
        label1.place(bordermode=OUTSIDE, height=100, width=99, x=0, y=0)
        label2 = Label(frame2, textvariable=self.b)
        label2.config(font=('Courier', 44))
        label2.place(bordermode=OUTSIDE, height=100, width=99, x=101, y=0)
        label3 = Label(frame2, textvariable=self.c)
        label3.config(font=('Courier', 44))
        label3.place(bordermode=OUTSIDE, height=100, width=99, x=201, y=0)
        label4 = Label(frame2, textvariable=self.d)
        label4.config(font=('Courier', 44))
        label4.place(bordermode=OUTSIDE, height=74, width=99, x=0, y=101)
        label5 = Label(frame2, textvariable=self.e)
        label5.config(font=('Courier', 44))
        label5.place(bordermode=OUTSIDE, height=74, width=99, x=101, y=101)
        label6 = Label(frame2, textvariable=self.f)
        label6.config(font=('Courier', 44))
        label6.place(bordermode=OUTSIDE, height=74, width=99, x=201, y=101)
        label7 = Label(frame2, textvariable=self.g)
        label7.config(font=('Courier', 44))
        label7.place(bordermode=OUTSIDE, height=45, width=99, x=0, y=201)
        label8 = Label(frame2, textvariable=self.h)
        label8.config(font=('Courier', 44))
        label8.place(bordermode=OUTSIDE, height=45, width=99, x=101, y=201)
        label9 = Label(frame2, textvariable=self.i)
        label9.config(font=('Courier', 44))
        label9.place(bordermode=OUTSIDE, height=45, width=99, x=201, y=201)
        label1.bind('<Button-1>', self.a1)
        label2.bind('<Button-1>', self.b1)
        label3.bind('<Button-1>', self.c1)
        label4.bind('<Button-1>', self.d1)
        label5.bind('<Button-1>', self.e1)
        label6.bind('<Button-1>', self.f1)
        label7.bind('<Button-1>', self.g1)
        label8.bind('<Button-1>', self.h1)
        label9.bind('<Button-1>', self.i1)
        exit_button = Button(frame4, text='Exit', command=quit)
        exit_button.pack(side=LEFT)
        reset_button = Button(frame4, text='Reset', command=self.reset)
        reset_button.pack(side=LEFT)
        Button(frame2, text='Press to initialise', command=self.initialise).pack(side=LEFT)
        self.name1 = 'Player 1'
        self.name2 = 'Player 2'
        self.times_used = 0
        self.toss = 0
        # Name2 GUI
        self.win_counter2 = 0
        self.name2_asterisk = ''
        self.name2_text = StringVar(value=f'{self.name2}{self.name2_asterisk}         {self.win_counter2}')
        self.name2_label = Label(root, textvariable=self.name2_text).pack(side=LEFT)
        # Name1 GUI
        self.win_counter1 = 0
        self.name1_asterisk = ''
        self.name1_text = StringVar(value=f'{self.name1}{self.name1_asterisk}         {self.win_counter1}')
        self.name1_label = Label(root, textvariable=self.name1_text).pack(side=LEFT)

    def turn_highlighter(self):
        if self.toss == 1 and self.counter in self.list1:
            self.name1_asterisk = '*'
            self.name2_asterisk = ''
        elif self.toss == 1 and self.counter in self.list2:
            self.name1_asterisk = ''
            self.name2_asterisk = '*'
        if self.toss == 2 and self.counter in self.list2:
            self.name1_asterisk = '*'
            self.name2_asterisk = ''
        elif self.toss == 2 and self.counter in self.list1:
            self.name1_asterisk = ''
            self.name2_asterisk = '*'
        self.update()

    def toss1(self):
        self.toss = randint(1, 2)
        if self.toss == 1:
            toss_window = Toplevel(root1)
            toss_window.geometry('210x200')
            Label(toss_window, text=f'{self.name1} has won the toss').pack()
        else:
            toss_window = Toplevel(root1)
            toss_window.geometry('210x200')
            Label(toss_window, text=f'{self.name2} has won the toss').pack()
        self.turn_highlighter()

    def update(self):
        self.name1_text.set(f'{self.name1}{self.name1_asterisk}         {self.win_counter1}')
        self.name2_text.set(f'{self.name2}{self.name2_asterisk}         {self.win_counter2}')

    def initialise(self):
        def name_getter():
            if self.times_used == 0:
                self.name1 = name_entry.get()
                name_entry.delete(0, END)
                a.set('Player 2 Enter Your Name')
                self.times_used += 1
            elif self.times_used == 1:
                self.name2 = name_entry.get()
                name_entry.delete(0, END)
                self.times_used = 2
                a.set('All Names are entered')
                self.a1flag = False
                self.b1flag = False
                self.c1flag = False
                self.d1flag = False
                self.e1flag = False
                self.f1flag = False
                self.g1flag = False
                self.h1flag = False
                self.i1flag = False
                self.update()
                window.destroy()
                self.toss1()
                self.turn_highlighter()

            else:
                window.destroy()

        window = Toplevel(root1)
        a = StringVar(value='Player 1 Enter Your Name')
        window.geometry('210x200')
        Label(window, textvariable=a).pack(side=TOP)
        Label(window, text='Name').pack(side=LEFT)
        name_entry = Entry(window)
        name_entry.pack(side=LEFT)
        Button(window, text='Submit', command=name_getter).pack(side=LEFT)
        if self.times_used == 2:
            a.set('Names are already entered')
            name_entry.insert(0, 'Already entered')

    def a1(self, event):
        if self.counter < 10 and not self.a1flag:
            self.a.set(utils.turn_finder(self.counter))
            self.counter += 1
            self.a1flag = True
        self.flag = utils.diagnols(self.a.get(), self.b.get(), self.c.get(), self.d.get(), self.e.get(), self.f.get(), self.g.get(), self.h.get(), self.i.get())
        if self.counter == 9 and not self.flag:
            self.draw_game()
        elif self.flag:
            self.end_game()
        self.turn_highlighter()

    def b1(self, event):
        if self.counter < 10 and not self.b1flag:
            self.b.set(utils.turn_finder(self.counter))
            self.counter += 1
            self.b1flag = True
        self.flag = utils.diagnols(self.a.get(), self.b.get(), self.c.get(), self.d.get(), self.e.get(), self.f.get(), self.g.get(), self.h.get(), self.i.get())
        if self.counter == 9 and not self.flag:
            self.draw_game()
        elif self.flag:
            self.end_game()
        self.turn_highlighter()

    def c1(self, event):
        if self.counter < 10 and not self.c1flag:
            self.c.set(utils.turn_finder(self.counter))
            self.counter += 1
            self.c1flag = True
        self.flag = utils.diagnols(self.a.get(), self.b.get(), self.c.get(), self.d.get(), self.e.get(), self.f.get(), self.g.get(), self.h.get(), self.i.get())
        if self.counter == 9 and not self.flag:
            self.draw_game()
        elif self.flag:
            self.end_game()
        self.turn_highlighter()

    def d1(self, event):
        if self.counter < 10 and not self.d1flag:
            self.d.set(utils.turn_finder(self.counter))
            self.counter += 1
            self.d1flag = True
        self.flag = utils.diagnols(self.a.get(), self.b.get(), self.c.get(), self.d.get(), self.e.get(), self.f.get(), self.g.get(), self.h.get(), self.i.get())
        if self.counter == 9 and not self.flag:
            self.draw_game()
        elif self.flag:
            self.end_game()
        self.turn_highlighter()

    def e1(self, event):
        if self.counter < 10 and not self.e1flag:
            self.e.set(utils.turn_finder(self.counter))
            self.counter += 1
            self.e1flag = True
        self.flag = utils.diagnols(self.a.get(), self.b.get(), self.c.get(), self.d.get(), self.e.get(), self.f.get(), self.g.get(), self.h.get(), self.i.get())
        if self.counter == 9 and not self.flag:
            self.draw_game()
        elif self.flag:
            self.end_game()
        self.turn_highlighter()

    def f1(self, event):
        if self.counter < 10 and not self.f1flag:
            self.f.set(utils.turn_finder(self.counter))
            self.counter += 1
            self.f1flag = True
        self.flag = utils.diagnols(self.a.get(), self.b.get(), self.c.get(), self.d.get(), self.e.get(), self.f.get(), self.g.get(), self.h.get(), self.i.get())
        if self.counter == 9 and not self.flag:
            self.draw_game()
        elif self.flag:
            self.end_game()
        self.turn_highlighter()

    def g1(self, event):
        if self.counter < 10 and not self.g1flag:
            self.g.set(utils.turn_finder(self.counter))
            self.counter += 1
            self.g1flag = True
        self.flag = utils.diagnols(self.a.get(), self.b.get(), self.c.get(), self.d.get(), self.e.get(), self.f.get(), self.g.get(), self.h.get(), self.i.get())
        if self.counter == 9 and not self.flag:
            self.draw_game()
        elif self.flag:
            self.end_game()
        self.turn_highlighter()

    def h1(self, event):
        if self.counter < 10 and not self.h1flag:
            self.h.set(utils.turn_finder(self.counter))
            self.counter += 1
            self.h1flag = True
        self.flag = utils.diagnols(self.a.get(), self.b.get(), self.c.get(), self.d.get(), self.e.get(), self.f.get(), self.g.get(), self.h.get(), self.i.get())
        if self.counter == 9 and not self.flag:
            self.draw_game()
        elif self.flag:
            self.end_game()
        self.turn_highlighter()

    def i1(self, event):
        if self.counter < 10 and not self.i1flag:
            self.i.set(utils.turn_finder(self.counter))
            self.counter += 1
            self.i1flag = True
        self.flag = utils.diagnols(self.a.get(), self.b.get(), self.c.get(), self.d.get(), self.e.get(), self.f.get(), self.g.get(), self.h.get(), self.i.get())
        if self.counter == 9 and not self.flag:
            self.draw_game()
        elif self.flag:
            self.end_game()
        self.turn_highlighter()

    def end_game(self):
        self.label_define.set('Winner Winner Chicken Dinner!')
        self.a1flag = True
        self.b1flag = True
        self.c1flag = True
        self.d1flag = True
        self.e1flag = True
        self.f1flag = True
        self.g1flag = True
        self.h1flag = True
        self.i1flag = True

    def draw_game(self):
        self.label_define.set('The Game has been Drawn!')
        self.a1flag = True
        self.b1flag = True
        self.c1flag = True
        self.d1flag = True
        self.e1flag = True
        self.f1flag = True
        self.g1flag = True
        self.h1flag = True
        self.i1flag = True

    def reset(self):
        self.a.set('')
        self.b.set('')
        self.c.set('')
        self.d.set('')
        self.e.set('')
        self.f.set('')
        self.g.set('')
        self.h.set('')
        self.i.set('')
        self.label_define.set('Results Pending...')
        self.counter = 0
        self.flag = False
        self.a1flag = False
        self.b1flag = False
        self.c1flag = False
        self.d1flag = False
        self.e1flag = False
        self.f1flag = False
        self.g1flag = False
        self.h1flag = False
        self.i1flag = False
        self.name2_asterisk = ''
        self.name1_asterisk = ''
        self.update()
        self.toss1()


root1 = Tk()
brit = TicTacToe(root1)
root1.mainloop()
