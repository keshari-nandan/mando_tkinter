from tkinter import *
from footer import Footer
from config import Config
from stats import Stats


class Project:
    def __init__(self, app):
        self.frame = LabelFrame(app.root, height=400, width=600, bg="snow2", text="Select Framework")
        self.frame.pack()
        self.footer = Footer(app, nextWin=Stats, prevWin=Config)

    def destroy(self):
        self.frame.destroy()
        self.footer.canvas.destroy()
