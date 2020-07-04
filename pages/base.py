from tkinter import *

class Base(object):
    """docstring for Base."""

    def __init__(self, root):
        self.top_frame = LabelFrame(root, width=450, height=50, pady=3, text="Configuration")
        self.center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)
        self.btm_frame = Frame(root, bg='white', width=450, height=45, pady=3)
        self.btm_frame2 = Frame(root, bg='lavender', width=450, height=60, pady=3)

        self.top_frame.grid(row=0, sticky="ew")
        self.center.grid(row=2, sticky="nsew")
        self.btm_frame.grid(row=4, sticky="ew")
        self.btm_frame2.grid(row=5, sticky="ew")
