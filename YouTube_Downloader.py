from tkinter import*
from pytube import YouTube
import tkinter as tk
root=tk.Tk()
root.title('YouTube Video Downloader')

canvas=tk.Canvas(root,height=500,width=450,bg='#d1d4f2')
canvas.pack()

link=StringVar()

def onbutton(e):
    button['bg']='grey'
def leavebutton(e):
    button['bg']='light grey'


label=Label(root,text='Spearton Youtube Video Downloader',bg='#d1d4f2',font=('Courier',16))
canvas.create_window(225,25,window=label)

label1=Label(root,text='Paste your link here',bg='#d1d4f2',font=('Courier',13))
canvas.create_window(225,200,window=label1)

entry=Entry(root,textvariable=link)
canvas.create_window(225,250,height=35,width=400,window=entry)

def downloader():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download()
    label2=Label(root,text='Video Downloaded',bg='#d1d4f2',font=('Courier',15))
    canvas.create_window(225,150,window=label2)

button=Button(root,text='Download',bd=0,bg='light grey',font=('Courier',20),command=downloader)
canvas.create_window(225,380,window=button)

button.bind('<Enter>',onbutton)
button.bind('<Leave>',leavebutton)
root.mainloop()
