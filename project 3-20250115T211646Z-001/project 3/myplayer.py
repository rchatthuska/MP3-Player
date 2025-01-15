import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
from pygame import mixer
from PIL import Image, ImageTk
import os
mixer.init()

class Player:
    def __init__(self):
        #creat Main window
        self.main_window = Tk()

        self.main_window.geometry('642x529')

        self.main_window.configure(bg='blue')

        #create welcome message
        self.label = Label(self.main_window, text = 'WELCOME TO MY MUSIC PLAYER' , font=('Ariel', 30) , foreground = 'white',
                           bg = 'blue')
        self.label.place(x=70,y=20)
        
        #create listbox
        self.menue = tkinter.LabelFrame(self.main_window)
        self.menue.pack()
        self.listbox = tkinter.Listbox(self.menue, height = 10, width=40)
        self.menue.place(x=70,y=132)

        
        self.listbox.pack(padx=10, pady=10)

        self.listbox.bind('<<Listboxselect>>')

        #creat scroll bar in listbox
        self.scrollbar1 = tkinter.Scrollbar(self.menue, orient=tkinter.VERTICAL)
        self.scrollbar1.pack(side='right', fill=tkinter.Y)
        self.scrollbar1.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar1.set)

        self.scrollbar2 = tkinter.Scrollbar(self.menue, orient=tkinter.HORIZONTAL)
        self.scrollbar2.pack(side='bottom', fill=tkinter.X)
        self.scrollbar2.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=self.scrollbar2.set)

        
        #Create add button
        self.frame3 = tkinter.LabelFrame(self.main_window, borderwidth = 0,)
        self.frame3.pack()
        self.add = tkinter.Button(self.frame3, text = 'add songs', borderwidth = 0,bd=0,
                                  command = self.Add_files ,foreground='orange')
        self.add.pack()
        self.frame3.place(x=70,y=100)

        #create remove button
        self.frame4 =  tkinter.Frame(self.main_window)
        self.frame4.pack()
        self.remove = tkinter.Button(self.frame4, text = 'remove songs',borderwidth = 0, bd=0,

                                  command = self.remove_files,foreground='orange')
        self.remove.pack()
        self.frame4.place(x=330, y=100)

        #create play button
        self.frame5 =  tkinter.Frame(self.main_window)
        self.frame5.pack()
        play_image1 = Image.open('play.png')
        play_image1= play_image1.resize((50,50), )
        play_image2=ImageTk.PhotoImage(play_image1)
        self.play = tkinter.Button(self.frame5,
                                   image=play_image2, bd = 0, borderwidth = 0,command = self.play)
        self.play.pack()
        self.frame5.place(x=140, y=377)
        
        #create pause button
        self.frame6 =  tkinter.Frame(self.main_window)
        self.frame6.pack()
        pause_image1 = Image.open('pause.png')
        pause_image1= pause_image1.resize((50,50), )
        pause_image2=ImageTk.PhotoImage(pause_image1)
        self.pause = tkinter.Button(self.frame6, image=pause_image2,borderwidth = 0,command = self.pause)
        self.pause.pack()
        self.frame6.place(x=350, y=377)

        #create resume button
        self.frame7 =  tkinter.Frame(self.main_window)
        self.frame7.pack()
        resume_image1 = Image.open('resume.png')
        resume_image1= resume_image1.resize((50,50), )
        resume_image2=ImageTk.PhotoImage(resume_image1)
        self.resume = tkinter.Button(self.frame7, image = resume_image2,borderwidth = 0, command = self.resume)
        self.resume.pack()
        self.frame7.place(x=420, y=377)

        #create volume scroll bar
        self.frame8 =  tkinter.LabelFrame(self.main_window, text='Vloume')
        self.frame8.pack()
        self.vloume_s = ttk.Scale(self.frame8,from_=0, to=1, orient=VERTICAL,
                                value = 1, command = self.volume ,length = 170)
        self.vloume_s.pack(pady=10)
        self.frame8.place(x=475, y=135)

        #create stop button
        self.frame9 =  tkinter.Frame(self.main_window)
        self.frame9.pack()
        stop_image1 = Image.open('stop.png')
        stop_image1= stop_image1.resize((50,50), )
        stop_image2=ImageTk.PhotoImage(stop_image1)
        self.stop = tkinter.Button(self.frame9, text = 'Stop', image=stop_image2, borderwidth = 0,command = self.stop)
        self.stop.pack()
        self.frame9.place(x=210, y=377)

        #create next button
        self.frame10 =  tkinter.Frame(self.main_window)
        self.frame10.pack()
        next_image1 = Image.open('next.png')
        next_image1= next_image1.resize((50,50), )
        next_image2=ImageTk.PhotoImage(next_image1)
        self.next = tkinter.Button(self.frame10, image = next_image2,borderwidth = 0,command = self.next_song)
        self.next.pack()
        self.frame10.place(x=280, y=377)

        #create previous button
        self.frame11 =  tkinter.Frame(self.main_window)
        self.frame11.pack()
        previous_image1 = Image.open('previous.png')
        previous_image1= previous_image1.resize((50,50), )
        previous_image2=ImageTk.PhotoImage(previous_image1)
        self.previous = tkinter.Button(self.frame11, image = previous_image2, borderwidth = 0,command = self.previos_song)
        self.previous.pack()
        self.frame11.place(x=70, y=377)

        #create quit button
        self.quit_button = tkinter.Button(self.main_window,bg='grey',
                                          text='QUIT',
                                          command =self.quit)
        self.quit_button.place(x=500, y=500)

       
        
        
        


        tkinter.mainloop()

    def Add_files(self):
        #this function iterate throug mp3 file in the directory
        #add them to the listbox
        self.filenames = askopenfilenames()
        for self.song in self.filenames:
            if self.song.endswith(".mp3"):
                self.listbox.insert(tkinter.END, self.song)

    def remove_files(self):
        #this function delete items from listbox
        #and stop playing them
        self.listbox.delete(tkinter.ACTIVE)
        mixer.music.stop()

    def play(self):
        #this function plays the current selected song
        mixer.music.load(self.listbox.get(ACTIVE))
        mixer.music.play(loops=0)

    def pause(self):
        #puase current selected song
        mixer.music.pause()

    def resume(self):
        #unpause current selected song
        mixer.music.unpause()

    def volume(self,x):
        #this function controls the voluem
        mixer.music.set_volume(self.vloume_s.get())

    def stop(self):
        #stop current playing music
        mixer.music.stop()

    def quit(self):
        #this fucntion quite the program
        #and stop the current play
        self.main_window.destroy()
        mixer.music.stop()

        
    def next_song(self):
        #return a tuple number
        self.select = self.listbox.curselection()
        if not self.select:
            tkinter.messagebox.showinfo('Alert','Please selct a song to play next')
        else:
            #add 1 to the current songs
            self.select = self.select[0]+1
            #grab song title from the playlist
            self.current = self.listbox.get(self.select)
            mixer.music.load(self.current)
            mixer.music.play(loops=0)
            #clear active bar
            self.listbox.selection_clear(0,END)
            self.listbox.activate(self.select)
            self.listbox.selection_set(self.select,last=None)
        

    def previos_song(self):
        #return a tuple number
        self.select = self.listbox.curselection()
        if not self.select:
            tkinter.messagebox.showinfo('Alert','Please selct a song to play previous')
        else:
            #add 1 to the current songs
            self.select = self.select[0]-1
            if self.select  < 0:
                tkinter.messagebox.showinfo('Alert','Wrong button')
            else:
                #grab song title from the playlist
                self.current = self.listbox.get(self.select)
                mixer.music.load(self.current)
                mixer.music.play(loops=0)
                #clear active bar
                self.listbox.selection_clear(0,END)
                self.listbox.activate(self.select)
                self.listbox.selection_set(self.select,last=None)

    
        

        

        
#Add_files()
if __name__ == '__main__':
    my_work = Player()
