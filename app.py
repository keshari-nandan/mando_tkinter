from tkinter import *
from win import Win
from footer import Footer


class App(Tk):

    def __init__(self, title=None):
        window_title = 'TheNandan'
        if title is not None:
            window_title = window_title + ' - ' + title
        super().__init__(className=window_title)
        self.window = Win(self)
        self.footer = Footer(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
