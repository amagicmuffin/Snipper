"""Snipper

This linux app built for the raspberry pi functions like window's snipping tool application.
"""

import tkinter as tk
import os

SCREENSHOT_DIRECTORY = '/home/pi'

class SnippingTool(master):
    """Main app. Creates and packs a button that can take a snip."""
    def __init__(self, master):
        self.snipButton = tk.Button(master,text = 'Snip',padx = 50,pady = 10,command = self.snip)
        
        self.snipButton.pack(master)
        
    def snip():
        """Take a snip. Check the length of /home/pi before and after the snip to make sure a new screenshot was added to that directory."""
        files = len(os.listdir(SCREENSHOT_DIRECTORY))
        os.system('scrot -s')
        if files < len(os.listdir(SCREENSHOT_DIRECTORY)): # check if a new screenshot was added
            snippingTool.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack()
    root.mainloop()
    
