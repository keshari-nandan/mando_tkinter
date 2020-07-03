from tkinter import *
from config import Config


class App:
    def __init__(self, title=None):
        self.root = Tk()
        window_title = 'TheNandan'
        if title is not None:
            self.root.title = window_title + ' - ' + title
        self.root.title(window_title)
        self.window = Config(self)
        self.root.mainloop()

    def switchWindow(self, window):
        self.window.destroy()
        self.window = window(self)
