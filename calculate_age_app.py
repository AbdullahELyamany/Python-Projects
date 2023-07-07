"""
 Created by *Abdullah EL-Yamany*

 Learn by 'Osama ELzero'
 Video Link ==>> https://youtu.be/eLRqoSXmLmk
 video title ==> Learn python By Examples - Ceare GUI Exe App To Calculate Age
 Note => In The End Video How to Convert the python file to .Exe

==========================
Calculate with Age Desktop App
With Tkinter
==========================
"""

from tkinter import *
from tkinter import messagebox

#------------------ function of Calculate Age -----------------#

def calc_age():

      #Get Age In Years
    age_value = age.get()

      #Get Time Units
    months = float(age_value) * 12
    weeks = months * 4
    days = float(age_value) * 365.25
    hour = days * 24
    minute = hour * 60
    second = minute * 60

    line_one = f"Your Age In Monthes Is: {int(months)}"
    line_two = f"Your Age In Weeks Is: {int(weeks)}"
    line_three = f"Your Age In Days Is: {int(days)}"
    line_four = f"Your Age In Hours Is: {int(hour)}"
    line_five = f"Your Age In Minutes Is: {minute}"
    line_six = f"Your Age In Seconds Is: {second}"


    all_lines = [line_one, line_two, line_three, line_four, line_five, line_six]

    messagebox.showinfo("Your Age In All Time Units", "\n".join(all_lines))



#------------------------- Gui Window ---------------------#

    # Create the Main App Window
age_app = Tk()

    # Change App Title/Name
age_app.title("Calculate Age App")

    # Set Dimensions
age_app.geometry('400x350')

    # Window Title Label
text = Label(age_app, text='Calculate Age App', font=('Arial', 20), height=2,fg='white', bg='black')
text.pack(fill=X) # Palce the text Into The window

    # Write Age Label
text = Label(age_app, text='Write You Age :', font=('Arial', 16),bg='white')
text.pack(pady=30) # Palce the text Into The window

    # Age Variables
age = StringVar()    # string variable Change, User Can update it        ##########################

    # set Default Value For Age
age.set("00.0")                                                       ######################

    # Create The Input For Age
age_input = Entry(age_app, width=4, font=("Arial, 20"), textvariable=age)    ####################
age_input.pack() # Palce the Input Into The window


    # Create The Calculate Button
btn = Button(
          age_app,
          text='Calculate Age',
          width=10,
          font=("Arial", 13),
          fg='white', 
          bg='blue',
          borderwidth=0,
          command=calc_age
      )
btn.pack(pady=15)



    # Run App Infinitely
age_app.mainloop()
