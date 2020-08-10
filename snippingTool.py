import tkinter as tk
import os

def snip():
    os.system('scrot -s') # take a snip



snippingTool = tk.Tk()

#snip button
snip = tk.snip(snippingTool,text = 'Snip',padx = 50,pady = 10,command = snip)
snip.pack()

#delay dropdown menu 
delay = Menubutton (top, text="Delay", relief=RAISED)
delay.grid()
delay.menu =  Menu ( mb, tearoff = 0 )
delay["menu"] =  mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

delay.menu.add_checkbutton ( label="mayo",
                          variable=mayoVar )
delay.menu.add_checkbutton ( label="ketchup",
                          variable=ketchVar )

snippingTool.mainloop()
