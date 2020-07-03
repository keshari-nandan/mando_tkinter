from tkinter import *
from footer import Footer

WINDOWS = [
    "Win", "Server"
]


class Language:
    def __init__(self, app):
        self.frame = LabelFrame(app.root, height=400, width=600, bg="snow2", text="Select Language")
        self.frame.pack()
        self.footer = Footer(app, nextWin=Framework)

    def destroy(self):
        self.frame.destroy()
        self.footer.canvas.destroy()


class Framework:
    def __init__(self, app):
        self.frame = LabelFrame(app.root, height=400, width=600, bg="snow2", text="Select Framework")
        self.frame.pack()
        self.footer = Footer(app, nextWin=Server, prevWin=Language)

    def destroy(self):
        self.frame.destroy()
        self.footer.canvas.destroy()


class Server:
    def __init__(self, app):
        self.frame = LabelFrame(app.root, height=400, width=600, bg="snow2", text="Select Server")
        self.frame.pack()
        self.footer = Footer(app, prevWin=Framework)

    def destroy(self):
        self.frame.destroy()
        self.footer.canvas.destroy()
