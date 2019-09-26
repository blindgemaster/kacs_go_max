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

    def clear(self):
        self.entry1.delete(0, END)


root1 = Tk()
ED = EncryptDecrypt(root1)
root1.mainloop()
