
"""
 Created by *Abdullah EL-Yamany*

 Channal => alba4mbarmg - الباشميرمج
 Video Link ==>> https://youtu.be/jjJ8U_hGjnQ

 note => Design and program Calculate App useing python language (Tkinter) | Python Project
"""
#==========================

from tkinter import *



expression = ""

def press(Input):

    global expression

    expression = expression + str(Input)

    equation.set(expression)


def equal_press():

    try:
        global expression
    
        result = str(eval(expression))
    
        equation.set(result)
    
        expression = ""
    except:
        equation.set('Enter Equation')
        expression = ""


def clear():

    global expression

    expression = ""

    equation.set("")


def delete():

    try:
        global expression
    
        expression = list(expression)
        n = len(expression) - 1
        n = expression[n]
        
        
        rever = expression.reverse()
        
        li = expression.remove(n)
        
        revers = expression.reverse()
    
        expression = "".join(expression)
    
        equation.set(expression)
    except:
        equation.set('')
        expression = ""



#----------------- Gui Window -----------------#

calculate_app = Tk()    # Create the Window App

calculate_app.title('Calculate')    # Title App In PC

calculate_app.geometry('450x600')   # Geometry App In PC


title_app = Label(calculate_app, text='Calculate', fg='blue', font=("Century 20 bold"))
title_app.grid(columnspan=4, padx=10, pady=20)


equation = StringVar()


entry_field = Entry(calculate_app, textvariable=equation)
entry_field.grid(columnspan=4, padx=10, pady=10, ipadx=540, ipady=20)


#----------------- Buttons ---------------------#

btn1 = Button(calculate_app, text='1', height=4, width=20, command= lambda: press(1))
btn1.grid(row=2, column=0, pady=2)

btn2 = Button(calculate_app, text='2', height=4, width=20, command= lambda: press(2))
btn2.grid(row=2, column=1)

btn3 = Button(calculate_app, text='3', height=4, width=20, command= lambda: press(3))
btn3.grid(row=2, column=2)


btn4 = Button(calculate_app, text='4', height=4, width=20, command= lambda: press(4))
btn4.grid(row=3, column=0, pady=2)

btn5 = Button(calculate_app, text='5', height=4, width=20, command= lambda: press(5))
btn5.grid(row=3, column=1)

btn6 = Button(calculate_app, text='6', height=4, width=20, command= lambda: press(6))
btn6.grid(row=3, column=2)


btn7 = Button(calculate_app, text='7', height=4, width=20, command= lambda: press(7))
btn7.grid(row=4, column=0, pady=2)

btn8 = Button(calculate_app, text='8', height=4, width=20, command= lambda: press(8))
btn8.grid(row=4, column=1)

btn9 = Button(calculate_app, text='9', height=4, width=20, command= lambda: press(9))
btn9.grid(row=4, column=2)


btn0 = Button(calculate_app, text='0', height=4, width=20, command= lambda: press(0))
btn0.grid(row=5, column=0, pady=2)

btn_dot = Button(calculate_app, text='.', height=4, width=20, command= lambda: press('.'))
btn_dot.grid(row=5, column=1)

btn_equal = Button(calculate_app, text='=', height=4, width=20, bg='blue', fg='white', command=equal_press)
btn_equal.grid(row=5, column=2)


btn_plas = Button(calculate_app, text='+', height=4, width=20, command= lambda: press('+'))
btn_plas.grid(row=2, column=3)

btn_minus = Button(calculate_app, text='–', height=4, width=20, command= lambda: press('-'))
btn_minus.grid(row=3, column=3)

btn_multiply = Button(calculate_app, text='×', height=4, width=20, command= lambda: press('*'))
btn_multiply.grid(row=4, column=3)

btn_divide = Button(calculate_app, text='÷', height=4, width=20, command= lambda: press('/'))
btn_divide.grid(row=5, column=3)

btn_clear = Button(calculate_app, text='Clear All', height=4, width=20, command= clear)
btn_clear.grid(row=6, column=0, pady=2)

btn_delete = Button(calculate_app, text='Delete', height=4, width=20, command= delete)
btn_delete.grid(row=6, column=1)









calculate_app.mainloop()
