from tkinter import *
import tkinter.messagebox as m

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alerButton = Button(self, text='hello', command=self.press)
        self.alerButton.pack()
        self.oneLabel = Label(self, text='study')
        self.oneLabel.pack()
        self.quitButton = Button(self, text='Quit',command=self.quit)
        self.quitButton.pack()

    def press(self):
        name = self.nameInput.get() or 'world'
        m.showinfo('Message','Hello,%s'%name)
app = Application()
app.master.title('hello world')
app.mainloop()

