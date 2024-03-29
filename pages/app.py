from tkinter import *
from .config import Config
from .project import Project
from .stats import Stats
import json

class App:
    def __init__(self, title=None):
        self.root = Tk()
        window_title = 'Mando'
        if title is not None:
            self.root.title = window_title + ' - ' + title
        self.root.title(window_title)
        self.root.minsize(500, 250)
        # self.root.geometry('{}x{}'.format(500, 250))
        if not self.getSystem():
            self.window = Config(self)
        elif not self.getProjects():
            self.window = Project(self)
        else:
            self.window = Stats(self)
        self.root.mainloop()

    def switchWindow(self, window):
        self.window.destroy()
        if window == 'stats':
            self.window = Stats(self)
        if window == 'config':
            self.window = Config(self)
        if window == 'project':
            self.window = Project(self)


    def getProjects(self):
        try:
            file_r = open("settings/projects.json", "r")
            projects = json.load(file_r)
            file_r.close()
        except Exception:
            return False
        return projects
    

    def getSystem(self):
        try:
            file_r = open("settings/system.json", "r")
            system = json.load(file_r)
            file_r.close()
        except Exception:
            return False
        return system