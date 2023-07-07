
"""
 GUI for Login/Signup Using Python and tkinter model

 Created by *Abdullah EL-Yamany*
"""

from tkinter import *


prog = Tk()


prog.title('Log In System')
prog.geometry('600x500')
prog.resizable(False, False)
#prog.iconbitmap('lock.png')


prog.config(background='#D5DBDB')

#---------title---------#
title = Label(prog, text='Log_in System', font=('Courier', 23), bg='black', fg='white')
title.pack(fill=X)

#---------frame---------#
fr1 = Frame(prog, width='1000', height='950', bg='whitesmoke')
fr1.pack(pady=60)

#---------Image---------#

photo = PhotoImage(file='lock_pass.png')
imo = Label(prog, image=photo)
imo.place(x=680, y=151)

#---------label---------#

lb1 = Label(fr1, text='UserName :', font=('Courier', 15), bg='whitesmoke')
lb1.place(x=10, y=600)

lb2 = Label(fr1, text='Password :', font=('Courier', 15), bg='whitesmoke')
lb2.place(x=10, y=685)

#---------Entry:---------#

en1 = Entry(fr1)
en1.place(x=290, y=615)

en2 = Entry(fr1)
en2.place(x=290, y=700)

#----------Buttons--------#

btn1 = Button(fr1, text='Log In', font=('Courier', 15), bg='white', width='9')
btn1.place(x=40, y=800)

btn2 = Button(fr1, text='Sign In', font=('Courier', 15), bg='white', width='9')
btn2.place(x=390, y=800)






prog.mainloop()