from tkinter import *
from .footer import Footer


class Project:
    def __init__(self, app):
        self.frame = LabelFrame(app.root, height=400, width=600, bg="snow2", text="Select Framework")
        self.frame.pack()
        self.footer = Footer(app, nextWin='stats', prevWin='config')

    def __str__(self):
        return 'project'

    def destroy(self):
        self.frame.destroy()
        self.footer.canvas.destroy()
