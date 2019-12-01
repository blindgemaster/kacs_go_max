from tkinter import *


class StopWatch:
    def __init__(self, root):
        self.seconds = 0
        self.pause = False
        root.geometry('300x200')
        root.title('Stopwatch by Khizar Asim')
        top_frame = Frame(root)
        top_frame.pack(side=TOP)
        heading_label = Label(top_frame, text='StopWatch')
        heading_label.pack(side=TOP)
        stopwatch_frame = Frame(root)
        stopwatch_frame.pack(side=TOP)
        stopwatch_values = Label(stopwatch_frame, text='00:00:00', font='courier')
        stopwatch_values.pack(side=LEFT)
        buttons_frame = Frame(root)
        buttons_frame.pack(side=BOTTOM)
        start_button = Button(buttons_frame, text='l>', command=self.start)
        pause_button = Button(buttons_frame, text='||', command=self.pause)
        stop_button = Button(buttons_frame, text='O')
        start_button.pack(side=LEFT)
        pause_button.pack(side=LEFT)
        stop_button.pack(side=LEFT)

    def start(self):
        while not self.pause:
            self.seconds += 1
            print(self.seconds)

    def pause(self):
        self.pause = True


root1 = Tk()
StopWatch(root1)
root1.mainloop()
