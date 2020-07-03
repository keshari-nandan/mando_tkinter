from tkinter import *
from footer import Footer
from project import Project


class Stats:
    def __init__(self, app):
        self.frame = LabelFrame(app.root, height=400, width=600, bg="snow2", text="Select Server")
        self.frame.pack()
        self.footer = Footer(app, prevWin=Project)

    def destroy(self):
        self.frame.destroy()
        self.footer.canvas.destroy()
