from tkinter import *
import random

app = Tk() 
app.title("ABCD") 

A = Label(app, text="A", width=12, bg='red')
A.pack(side='top',fill=X, expand=1)
B = Label(app, text="B", width=12, bg='yellow')
B.pack(side='bottom')
C = Label(app, text="C", width=12, bg='blue')
C.pack(side='left', fill=Y, expand=1)
D = Label(app, text="D", width=12, bg='white')
D.pack(side='right')



app = Tk()
app.title("ABCD2") 

lFrame = Frame(app)
rFrame = Frame(app)
lFrame.pack(side='left',fill=BOTH, expand=1)
rFrame.pack(side='right',fill=BOTH, expand=1)

b1 = Label(lFrame, text="A", bg='blue', width=12)
b1.pack(side='top', fill=BOTH, expand=1)
b2 = Label(lFrame, text="B", bg='white', width=12)
b2.pack(side='bottom', fill=BOTH, expand=1)
b3 = Label(rFrame, text="C", bg='white', width=12)
b3.pack(side='top', fill=BOTH, expand=1)
b4 = Label(rFrame, text="D", bg='blue', width=12)
b4.pack(side='bottom', fill=BOTH, expand=1)


app.mainloop()

