"""
 Created by *Abdullah EL-Yamany*

 Channal => alba4mbarmg - الباشميرمج
 Video Link ==>> https://youtu.be/Gnq6RQw1Ca4

 note => Design and program play sound App useing python language (Tkinter)
"""

#===============================


from tkinter import *
from tkinter import filedialog
from pygame import mixer


#--------------- Add Song ----------------#
def addSongs():

    songsSelection = filedialog.askopenfilenames(initialdir="Music/",
                         title="Chosse Songs",
                         filetypes=(("mp3 files", "*.mp3"),)
                     )
    for s in songsSelection :
        
        s = s.replace("/storage.emulated/0/Download/git/play_songs/Music/", " ")
        listSongs.insert(END, s)



#--------------- Delete Song ----------------#

def delete_song():
    currSong = listSongs.curselection()
    listSongs.delete(currSong[0])
    


#---------------- Play Song Btn ---------------#

def play_song():

    song = listSongs.get(ACTIVE)
    #song = f"{song}"

    mixer.music.load(f"{song}")
    mixer.music.play()
    

#---------------- Stop Song Btn ---------------#

def stop_song():

    mixer.music.stop()
    listSongs.selection_clear(ACTIVE)


#-------------- Pause Song Btn --------------#

def pause_song():
    mixer.music.pause()


#-------------- Resume Song Btn --------------#

def resume_song():
    mixer.music.unpause()


#-------------- Prev Song Btn --------------#

def prev_song():
    prev = listSongs.curselection()
    prev = prev[0]-1
    song = listSongs.get(prev)
    song = f"{song}"
    mixer.music.load(song)
    mixer.music.play()
    listSongs.selection_clear(0, END)
    listSongs.activate(prev)
    listSongs.selection_set(prev)


#-------------- Next Song Btn--------------#

def next_song():
    next = listSongs.curselection()
    next = next[0] + 1
    song = listSongs.get(next)
    mixer.music.load(f"{song}")
    mixer.music.play()
    listSongs.selection_clear(0, END)
    listSongs.activate(next)
    listSongs.selection_set(next)
    

#--------------- GUI Tkinter ----------------#

window = Tk()
window.title('Play Sound')


mixer.init()


my_menu = Menu(window)
window.config(menu=my_menu)
control_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=control_song_menu, font=('arial', 16))

control_song_menu.add_command(label="Add Song", font=('arial', 14), command=addSongs)
control_song_menu.add_command(label="Delete Song", font=('arial', 14), command=delete_song)


#------------- List GUI To Add Music in This ------------------#

listSongs = Listbox(window,
                bg='black',
                fg='white',
                font=('arial', 13),
                width=83,
                height=18,
                selectmode=SINGLE,
                selectbackground='gray',
                selectforeground='black'
            )
listSongs.grid(columnspan=12)


#------------------ Buttons ------------------#

playBtn = Button(window, text='Play', font=('arial', 15), width=10, height=2, command=play_song)
playBtn.grid(row=1, column=0, pady =8)

pauseBtn = Button(window, text='Pause', font=('arial', 15), width=10, height=2, command=pause_song)
pauseBtn.grid(row=1, column=1)

stopBtn = Button(window, text='Stop', font=('arial', 15), width=10, height=2, command=stop_song)
stopBtn.grid(row=1, column=2)

resumeBtn = Button(window, text='Resume', font=('arial', 15), width=10, height=2, command=resume_song)
resumeBtn.grid(row=1, column=3)

prevBtn = Button(window, text='Prev  ⏮', font=('arial', 15), width=10, height=2, command=prev_song)
prevBtn.grid(row=1, column=4)

nextBtn = Button(window, text='Next  ⏭', font=('arial', 15), width=10, height=2, command=next_song)
nextBtn.grid(row=1, column=5)




window.mainloop()
