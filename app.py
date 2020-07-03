from tkinter import *


class App(Tk):

    def __init__(self, title=None):
        window_title = 'TheNandan'
        if title is not None:
            window_title = window_title + ' - ' + title
        super().__init__(className=window_title)
        self.frame = Frame(self, height=400, width=600)
        self.frame.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
