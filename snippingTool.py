import tkinter as tk
import os

def snip():
    files = len(os.listdir('/home/pi'))
    os.system('scrot -s')
    if files < len(os.listdir('/home/pi')): # check if a new screenshot was added
        snippingTool.destroy()


snippingTool = tk.Tk()

button = tk.Button(snippingTool,text = 'Snip',padx = 50,pady = 10,command = snip)
button.pack()

snippingTool.mainloop()
