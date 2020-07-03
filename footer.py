from tkinter import Canvas, Button, X, BOTTOM


class Footer:

    def __init__(self, master):
        self.canvas = Canvas(master, bg="white", height=60)
        self.canvas.pack(fill=X, side=BOTTOM)
        self.next_btn = Button(master, text="Next")
        self.next_btn.place(relx=0.9, rely=0.9)
