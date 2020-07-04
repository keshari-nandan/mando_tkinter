from tkinter import *

class Base(object):
    """docstring for Base."""

    def __init__(self, app, text="Mando Setup"):
        self.app = app
        self.top_frame = LabelFrame(app.root, width=450, height=50, pady=3, text=text)
        self.center = Frame(app.root, width=50, height=40, padx=3, pady=3)
        # self.btm_frame = Frame(root, bg='white', width=450, height=45, pady=3)
        # self.btm_frame2 = Frame(root, bg='lavender', width=450, height=60, pady=3)

        self.top_frame.grid(row=0, sticky="ew")
        self.center.grid(row=7, sticky="e")
        # self.btm_frame.grid(row=4, sticky="ew")
        # self.btm_frame2.grid(row=5, sticky="ew")

        # layout all of the main containers
        app.root.grid_rowconfigure(1, weight=1)
        app.root.grid_columnconfigure(0, weight=1)


    def destroy(self):
        self.top_frame.destroy()
        self.center.destroy()
