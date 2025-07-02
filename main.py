from tkinter import *
import tkinter.font
import helper

colors = ['blue', 'red', 'yellow', 'green']

def spin(*args):
    return

root = Tk()
root.title("Project Spinner")
root.geometry('1280x720')

spinner, spinner_center, spinner_radius = helper.create_spinner(root, 640, 720, colors=colors)

spinner.place(x=100, y=0)

font_title = tkinter.font.Font(size=25)
font_button = tkinter.font.Font(size=16)

cfg_title = Label(root, text="Settings", font=font_title)
cfg_title.place(x=950, y=10)

spin_btn = Button(root, text="Spin!", font=font_button, command=spin, height=1, width=10)
spin_btn.place(x=940, y=600)

root.bind("<Return>", spin)

root.mainloop()