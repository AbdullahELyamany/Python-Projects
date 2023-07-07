
"""
 Created by *Abdullah EL-Yamany*

 Network Monitoring Program

 Channal => CodeRK-ركوان للبرمجه
 Link Video => https://youtu.be/rJXluycuy4o
"""

#=====================

from tkinter import *
import tkinter.scrolledtext as scrl_t
import scapy.all as sc
from scapy.layers import http
import threading
import time



## ========================= Functions of App ===================== ##

#------------ Button Function & Text Area -------------#

def net():

    time.sleep(5)

    def sn(interface):

        sc.sniff(iface=interface, store=False, prn=prosses)

    def prosses(packet):

        if packet.haslayer(http.HTTPRequest):

              #-------------- TXT -----------#
            txt.insert('end', "[+]", 'zero')
            txt.insert('end', packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path, 'one')
            txt.insert('end', "\n")

            if packet.haslayer(sc.Raw):

                data = packet[sc.Raw].load

                txt.insert('end', "[+]", 'three')
                txt.insert('end', data, 'two')
                txt.insert('end', "\n")

                  #-------------- TXT1 -----------#
                txt1.delete('1.0', END)
                txt1.insert('end', txt.index('end-1c').split('.')[0])


    sn("Wi-Fi")
    #sn("Ethernet6") # 1 -> 6
    #sn("Wlan0")




## ========================= Design Gui ===================== ##


app = Tk()

app.title('Networking App')  # Title Window in PC

app.geometry('1000x800')  # Size Window in PC

app.configure(background='whitesmoke') # background of App


title = Label(app,
    text='Network Security App -- [ELYAMANY]',
    font=("Courier", 18),
    bg='black',
    fg='White'
)
    # Title of App
title.pack(fill=X)


#------------------- Text & Scroll ---------------#

txt = scrl_t.ScrolledText(app)
txt['font'] = ("Courier", '14', 'bold')
txt.place(x=1, y=80, width=1200, height=980)
#-------- Text Colors --------#
txt.tag_config('zero', background='white', foreground='red')
txt.tag_config('one', background='white', foreground='black')
txt.tag_config('two', background='gray', foreground='yellow')
txt.tag_config('three', background='white', foreground='green')

#------------------- Image ---------------#

photo = PhotoImage(file="/storage/emulated/0/python/project/min-app/gui_tkinter/net_sec/image_net.png")

panel = Label(app, image=photo)

panel.place(x=1205, y=80, width="690", height="990")


#------------------ Button --------------#

button = Button(app,
    text='Network monitoring started', 
    width=25, 
    height=2, 
    cursor='hand2', 
    command=threading.Thread(target=net).start()
)
button.place(x=10, y=1070)


#------------------ Label + text count --------------#

label = Label(app, text='The number of interactions you\'ve done', font=("Courier", 10, 'bold'))
label.place(x=440, y=1093)


txt1 = scrl_t.ScrolledText(app)
txt1['font'] = ("Courier", '10', 'bold')
txt1.place(x=1180, y=1093, width=90, height=45)



app.mainloop()

