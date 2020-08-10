import tkinter as tk
import os

#wtf is going on go google how to do a dropdown

def snip():
    os.system('scrot -s') # take a snip



snippingTool = tk.Tk()
#snippingTool.title('Snipper')

#snip button
snip = tk.Button(snippingTool,text = 'Snip',padx = 50,pady = 10,command = snip)
snip.pack()

#delay dropdown menu 
mainframe = tk.Frame(snippingTool)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

snippingTool.mainloop()
