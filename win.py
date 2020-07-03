from tkinter import *
from footer import Footer

WINDOWS = [
    "Win", "Server"
]


class Win:
    def __init__(self, app):
        self.frame = LabelFrame(app.root, height=400, width=600, bg="snow2", text="Win")
        self.frame.pack()
        self.footer = Footer(app, nextWin=Server)

    def destroy(self):
        self.frame.destroy()
        self.footer.canvas.destroy()


class Server:
    def __init__(self, app):
        self.frame = LabelFrame(app.root, height=400, width=600, bg="snow2", text="Server")
        self.frame.pack()
        self.footer = Footer(app, prevWin=Win)

    def destroy(self):
        self.frame.destroy()
        self.footer.canvas.destroy()
