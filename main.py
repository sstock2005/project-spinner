from tkinter import *
import tkinter.font
import helper
import random
import time

colors = ['blue', 'red', 'yellow', 'green']

spun_language = False
spun_project = False
spun_last_frame = 0

def spin_spinner(*args):
    """Function to animate our spinner with the help of helper.spin
    """
    
    global spun_last_frame
    
    frames = range(0, 8)
    ending_count = random.randint(50, 200)
    
    while (ending_count % 2) == 0:
        ending_count = random.randint(50, 200)
        
    c = 0
    while True:
        for _ in range(0, 2):
            for frame in frames:
                spinner = helper.spin(root, frame, 640, 720, colors)
                spinner.place(x=100, y=0)
                spun_last_frame = frame
                
                if c > ending_count * 0.5:
                    time.sleep(0.1)
                    
                elif c > ending_count * 0.7:
                    time.sleep(0.8)
                    
                elif c >= ending_count * 0.8:
                    time.sleep(1)
                    
                else:
                    time.sleep(0.05)
                    
                root.update()
                
                if c == ending_count:
                    return
                
                c += 1
                
def button_logic(*args):
    """The name says it all. (It's button logic)
    """
    
    global spun_language
    global spun_project
    
    root: Canvas = args[0]
    
    if spun_language and spun_project:
        Label(root, text=f"Language:                            ", font=font_cfg_label).place(x=950, y=80)
        Label(root, text=f"Project:                             ", font=font_cfg_label).place(x=950, y=120)
        spun_language = False
        spun_project = False
        
    spin_spinner(args)
    
    if not spun_language or not spun_project:
        if not spun_language:
            language, _ = helper.color2config(helper.frame2color(spun_last_frame))
            Label(root, text=f"Language: {language}", font=font_cfg_label).place(x=950, y=140)
            spun_language = True
            
        else:
            color = helper.frame2color(spun_last_frame)
            _, projects = helper.color2config(color)
            project = helper.color2proj(color, projects)
            Label(root, text=f"Project: {project}", font=font_cfg_label).place(x=950, y=170)
            spun_project = True


root = Tk()
root.title("Project Spinner")
root.geometry('1280x720')

spinner = helper.spin(root, spun_last_frame, 640, 720, colors).place(x=100, y=0)

font_title = tkinter.font.Font(size=25)
font_button = tkinter.font.Font(size=16)
font_winner_label = tkinter.font.Font(size=12)
font_cfg_label = tkinter.font.Font(size=16)

Label(root, text="Results", font=font_title).place(x=1050, y=50)
Label(root, text="Language:", font=font_cfg_label).place(x=950, y=140)
Label(root, text="Project:", font=font_cfg_label).place(x=950, y=170)
Button(root, text="Spin!", font=font_button, command=lambda: button_logic(root), height=1, width=10).place(x=1000, y=400)

root.bind("<Return>", lambda: button_logic(root))

root.mainloop()