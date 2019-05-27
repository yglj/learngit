'''
tk是一个图形库，支持多操作系统，用tcl语言开发
tk会调用操作系统提供的本地gui接口
python调用内置的tk，访问封装的接口
'''

from tkinter import *
import tkinter.messagebox as messagebox

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text='进行简易的四则运算!')
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self,text='计算',command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        try:
            name = eval(name)
        except Exception:
            messagebox.showinfo('error','输入格式错误')
        else:
            messagebox.showinfo('message','result:%s'%name)



app = App()
app.master.title('简易计算器')
app.master.geometry('300x100')
app.mainloop()
