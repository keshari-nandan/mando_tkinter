from tkinter import *
from project import Project
from footer import Footer


class Config:
    def __init__(self, app):
        self.frame = LabelFrame(app.root, height=400, width=600, bg="snow2", text="Configuration")
        self.frame.pack()
        self.footer = Footer(app, nextWin=Project)

    def destroy(self):
        self.frame.destroy()
        self.footer.canvas.destroy()
