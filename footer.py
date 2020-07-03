from tkinter import *


class Footer:
    def __init__(self, app, nextWin=None, prevWin=None):
        self.app = app
        self.nextWin = nextWin
        self.prevWin = prevWin
        self.canvas = Canvas(app.root, bg="white", height=60)
        self.canvas.pack(fill=X, side=BOTTOM)
        if nextWin:
            self.next_btn = Button(self.canvas, bg="blue", fg="white", text="Next", command=self.nextWindow)
            self.next_btn.pack(side=RIGHT)
        if prevWin:
            self.next_btn = Button(self.canvas, bg="white", fg="gray", text="Prev", command=self.prevWindow)
            self.next_btn.pack(side=RIGHT)

    def nextWindow(self):
        if self.nextWin:
            self.app.switchWindow(self.nextWin)

    def prevWindow(self):
        if self.prevWin:
            self.app.switchWindow(self.prevWin)
