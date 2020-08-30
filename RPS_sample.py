#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 08:11:32 2020

@author: sanyoon
"""

import tkinter as tk
import random
from PIL import Image, ImageTk
from playsound import playsound


def showImg(frame, choice):
    if choice == "rock":
        load = Image.open("/Users/sanyoon/Desktop/rock.png")
    elif choice == "paper":
        load = Image.open("/Users/sanyoon/Desktop/paper.png")
    elif choice == "scissor":
        load = Image.open("/Users/sanyoon/Desktop/scissor.png")
    render = ImageTk.PhotoImage(load)
    # labels can be text or images
    img = tk.Label(frame, image=render)
    img.image = render
    img.place(x=150, y=150)

# Game logic
def compare(p_choice, c_choice):
    if (p_choice == c_choice):
        p_label["text"] = "Player has " + p_choice
        c_label["text"] = "Computer has " + c_choice
        m_label["text"] = "Tie!"
        showImg(p_frame, p_choice)
        showImg(c_frame, c_choice)
    elif (p_choice == "paper"):
        if (c_choice == "rock"):
            p_label["text"] = "Player has " + p_choice
            c_label["text"] = "Computer has " + c_choice
            m_label["text"] = "Player Wins!"
            showImg(p_frame, p_choice)
            showImg(c_frame, c_choice)
        else:
            p_label["text"] = "Player has " + p_choice
            c_label["text"] = "Computer has " + c_choice
            m_label["text"] = "Computer Wins!"
            showImg(p_frame, p_choice)
            showImg(c_frame, c_choice)
    elif (p_choice == "scissor"):
        if (c_choice == "paper"):
            p_label["text"] = "Player has " + p_choice
            c_label["text"] = "Computer has " + c_choice
            m_label["text"] = "Player Wins!"
            showImg(p_frame, p_choice)
            showImg(c_frame, c_choice)
        else:
            p_label["text"] = "Player has " + p_choice
            c_label["text"] = "Computer has " + c_choice
            m_label["text"] = "Computer Wins!"
            showImg(p_frame, p_choice)
            showImg(c_frame, c_choice)
    elif (p_choice == "rock"):
        if(c_choice == "scissor"):
            p_label["text"] = "Player has " + p_choice
            c_label["text"] = "Computer has " + c_choice
            m_label["text"] = "Player Wins!"
            showImg(p_frame, p_choice)
            showImg(c_frame, c_choice)
        else:
            p_label["text"] = "Player has " + p_choice
            c_label["text"] = "Computer has " + c_choice
            m_label["text"] = "Computer Wins!"
            showImg(p_frame, p_choice)
            showImg(c_frame, c_choice)

# Player chooses rock
def rock(event):
    p_choice = "rock"
    c_choice = options[random.randint(0,2)]
    compare(p_choice, c_choice)
    
# Player chooses paper  
def paper(event):
    p_choice = "paper"
    c_choice = options[random.randint(0,2)]
    compare(p_choice, c_choice)

# Player chooses scissor
def scissor(event):
    p_choice = "scissor"
    c_choice = options[random.randint(0,2)]
    compare(p_choice, c_choice)
    
    

window = tk.Tk()
options = ['rock','paper', 'scissor']
#playsound("/Users/sanyoon/Downloads/rps_music.mp3")

main_frame = tk.Frame(master=window, width=200, height = 60, bg="blue")

#rock button
rck_btn = tk.Button(main_frame, text = "ROCK", bg = "red", fg = "green")
rck_btn.bind("<Button-1>", rock)
rck_btn.pack(side = tk.LEFT)

#paper button
ppr_btn = tk.Button(main_frame, text = "PAPER", bg = "red", fg = "blue")
ppr_btn.bind("<Button-1>", paper)
ppr_btn.pack(side = tk.LEFT)

#scissor button
ssr_btn = tk.Button(main_frame, text = "SCISSOR", bg = "red", fg = "red")
ssr_btn.bind("<Button-1>", scissor)
ssr_btn.pack(side = tk.LEFT)

# Main label
m_label = tk.Label(main_frame, text = "Let's Play Rock, Paper, Scissor!")
m_label.place(x=50, y=50)

# MAIN FRAME PACK
main_frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)  


p_frame = tk.Frame(master=window, width=100, height= 400, bg="red")

# Player label
p_label = tk.Label(p_frame, text = "Player Screen")
p_label.place(x=50, y=50)

# PLAYER FRAME PACK
p_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

c_frame = tk.Frame(master=window, width=100, height = 400, bg="yellow")
# Computer label
c_label = tk.Label(c_frame, text = "Computer Screen")
c_label.place(x=50, y=50)

# COMPUTER FRAME PACK
c_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

## Show image
#load = Image.open("/Users/sanyoon/Desktop/tattoo/simpson.png")
#render = ImageTk.PhotoImage(load)
## labels can be text or images
#img = tk.Label(mase"p_frame", image=render)
#img.image = render
#img.place(x=50, y=50)


window.mainloop()