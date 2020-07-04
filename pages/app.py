from tkinter import *
from .config import Config
from .project import Project
from .stats import Stats


class App:
    def __init__(self, title=None):
        self.root = Tk()
        window_title = 'Mando'
        if title is not None:
            self.root.title = window_title + ' - ' + title
        self.root.title(window_title)
        # self.root.geometry('{}x{}'.format(500, 250))
        self.window = Config(self)
        self.root.mainloop()

    def switchWindow(self, window):
        self.window.destroy()
        if window == 'stats':
            self.window = Stats(self)
        if window == 'config':
            self.window = Config(self)
        if window == 'project':
            self.window = Project(self)
