"""Used libraries"""
import tkinter as tkr
from tkinter import *
import pandas as pd
import pygame
import os
import matplotlib
from matplotlib import  pyplot as plt
matplotlib.use("TkAgg")


"""Initialization"""
pygame.init()
pygame.mixer.init()
pygame.display.init()

"""Window"""
player = Tk()

""""Window settings"""
player.title("Player")
player.geometry("300x440")

"""CSV file to be showed"""
file=pd.read_csv('C:\\Users\\bkoka\\OneDrive\\Documents\\MinutesWeek.csv')
file

"""Playlist folder"""
os.chdir("D:\PythonFiles\Songs")
print(os.getcwd)
songlist = os.listdir()

"""Volume control"""
Volume = tkr.Scale(player, from_=0.0,to_=1.0,
                   orient = tkr.HORIZONTAL, resolution = 0.01)

"""Playlist"""  
playlist = tkr.Listbox(player, selectmode = tkr.SINGLE)
print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

"""Actions"""
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(Volume.get())
    print(pygame.mixer.music.set_volume())
    print(Volume.get())
    pygame.mixer.music.rewind()

def Pause():
    pygame.mixer.music.pause()

def Resume():
    pygame.mixer.music.unpause()

def MinutesWeek():
    minutes_y = file['Minutes'];
    days_x = file['Days of week']
    plt.plot(days_x, minutes_y, 'k--o', label='Minutes played per week')
    plt.show()



    """Buttons"""

"""Play button"""
Play = tkr.Button(player, width = 5, height = 3, text = "Play", command=Play)
Play.pack(fill="x")
"""Pause button"""
Pause = tkr.Button(player, width = 5, height = 3, text = "Pause", command=Pause)
Pause.pack(fill="x")
"""Resume button"""
Resume = tkr.Button(player, width = 5, height = 3, text = "Resume", command=Resume)
Resume.pack(fill="x")
"""Show plot from CSV file"""
MinutesWeek = tkr.Button(player, width=5, height=3, text="Show data", command=MinutesWeek)
MinutesWeek.pack(fill="x")


"""Songs names"""
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable = var)

"""Widgets"""
Volume.pack(fill="x")
songtitle.pack()
playlist.pack(fill="both", expand="yes")

"""Activate"""
player.mainloop()