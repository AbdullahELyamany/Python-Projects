
"""
 Created by *Abdullah EL-Yamany*

 Channal => alba4mbarmg - الباشميرمج
 Video Link ==>> https://youtu.be/_qMGOoyL8zA

 note => Design and program Alarm App useing python language (Tkinter)
"""
#==========================

from tkinter import *
import datetime
import time
#import winsound
import threading



def Threading():

    t1 = threading.Thread(target=alarm)
    t1.start()




def alarm():

    while True:

        if hour.get() == minute.get() == second.get() == "00" :

            state.config(text="Please, Select Time!", bg="red")
            break

        else:
            state.config(text="Please, Select Time!", bg="green")
            userTime = f"{hour.get()}:{minute.get()}:{second.get()}"
        
            time.sleep(1)
        
            current_time = datetime.datetime.now().strftime("%H:%M:%S")


            if userTime == current_time :
    
                state.config(text="Time To Wake Up!", bg="black")
                winsound.PlaySound(
                    "/sdcard/python/project/min-app/gui_tkinter/alba4mbrmg/alarm/Alarm.mp3"
                )

                hour.set(hours[0])
                minute.set(minutes[0])
                second.set(seconds[0])
                break
    

#--------------------------------- Gui Window ------------------------------#


alarm_app = Tk()    # Create the Window App

alarm_app.geometry('700x450')    # Size Wimdow in PC

alarm_app.title("Alarm App")    # Title App in PC

icon_frame = PhotoImage(file=r"/sdcard/python/project/min-app/gui_tkinter/alba4mbrmg/alarm/img/icon.png")    # Icon App in PC
alarm_app.iconphoto(False, icon_frame)



app_title = Label(alarm_app, text="Alarm Clock", font=("Century 30 bold"), bg="black", fg="white")
app_title.pack(fill=X)

set_time = Label(alarm_app, text="Set Time", font=("Century 24"))
set_time.pack(pady=20)



#=========== Frame of [Hours, Min, Second]

frame = Frame(alarm_app)
frame.pack()

#---------- Hours --------#
hour = StringVar(alarm_app)

hours = []

for i in range(25):
    hours.append(str(i).zfill(2))

hours_menu = OptionMenu(frame, hour, *hours)
hours_menu.pack(side=LEFT)
hours_menu.config(font=("Century 13"), width=5, background="white")
hour.set(hours[0])


#---------- Minutes --------#
minute = StringVar(alarm_app)

minutes = []

for i in range(61):
    minutes.append(str(i).zfill(2))

mins_menu = OptionMenu(frame, minute, *minutes)
mins_menu.pack(side=LEFT)
mins_menu.config(font=("Century 13"), width=5, background="white")
minute.set(minutes[0])


#---------- Seconds --------#
second = StringVar(alarm_app)

seconds = []

for i in range(61):
    seconds.append(str(i).zfill(2))

secs_menu = OptionMenu(frame, second, *seconds)
secs_menu.pack(side=LEFT)
secs_menu.config(font=("Century 13"), width=5, background="white")
second.set(seconds[0])


#------------ Botton To Start App ------------#

btn = Button(alarm_app, text="Start Alarm", font=("Century 18 bold"), bg="blue", fg="white", command=Threading)
btn.pack(pady=50)


#------ ----#

state = Label(alarm_app, font=("Century 10 bold"), fg="white")
state.pack()









alarm_app.mainloop()
