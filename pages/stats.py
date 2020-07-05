from tkinter import *
from .base import Base


class Stats(Base):
    def __init__(self, app):
        super().__init__(app, "Dashboard")
        

                # Bottom of page
        row, column = app.root.grid_size()
        next_btn = Button(self.center, text="Quit", fg="white", bg="RoyalBlue1", activebackground="RoyalBlue2",
                            relief="flat", width="12", cursor="hand1")
        next_btn.grid(row=row, column=column, sticky="e")
        back_btn = Button(self.center, text="Projects", relief="flat", width="12", cursor="hand1", command=self.previousPage)
        back_btn.grid(row=row, column=column - 1,sticky="w")
    

    def previousPage(self):
        self.app.switchWindow('project')