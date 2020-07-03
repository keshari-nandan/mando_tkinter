from tkinter import *
from .footer import Footer


class Stats:
    def __init__(self, app):
        self.frame = LabelFrame(app.root, height=400, width=600, bg="snow2", text="Select Server")
        self.frame.pack()
        self.footer = Footer(app, prevWin='project')

    def __str__(self):
        return 'stats'

    def destroy(self):
        self.frame.destroy()
        self.footer.canvas.destroy()
