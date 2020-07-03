from tkinter import *
from win import Win


class App:
    def __init__(self, title=None):
        self.root = Tk()
        window_title = 'TheNandan'
        if title is not None:
            self.root.title = window_title + ' - ' + title
        self.root.title(window_title)
        self.window = Win(self)

    def switchWindow(self, window):
        self.window.destroy()
        self.window = window(self)


if __name__ == "__main__":
    app = App()
    app.root.mainloop()
