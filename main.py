from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


#function
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('downloading!!!!')
    #download video
    mp4_video= YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move to selected
    shutil.move(mp4_video, user_path)
    screen.title('download complete! download again')



screen = Tk()
title = screen.title('Youtube download')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image
logo_img = PhotoImage(file='yt.png')
#resize
logo_img = logo_img.subsample(2 , 2)

canvas.create_image(250,80, image=logo_img)


#link field

link_field = Entry(screen, width=50)
link_label = Label(screen, text = "enter download link:", font={'Arial',20})

#select path for saving the video

path_label = Label(screen,text= "Select Path For Download", font={'Arial',20})
select_btn = Button(screen, text="Select", command=select_path)

#add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250,330,window=select_btn)

#add widgets to window
canvas.create_window(250, 170, window= link_label)
canvas.create_window(250, 220, window= link_field)

#button
download_btn = Button(screen, text='start downloading', command=download_file)
##add tocanvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()