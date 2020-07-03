from tkinter import *
from wins import Language


class App:
    def __init__(self, title=None):
        self.root = Tk()
        window_title = 'TheNandan'
        if title is not None:
            self.root.title = window_title + ' - ' + title
        self.root.title(window_title)
        self.window = Language(self)

    def switchWindow(self, window):
        self.window.destroy()
        self.window = window(self)


if __name__ == "__main__":
    app = App()
    app.root.mainloop()
