from tkinter import *
from .footer import Footer
from .base import Base


class Config(Base):
    def __init__(self, app):
        root = app.root
        self.languages = ['Php', 'Python']
        self.frameworks = ["Laravel", "Core Php"]
        self.versions = []
        super().__init__(root)

        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)



        # Top Frame Configuration
        lang_label = Label(self.top_frame, text='Programming Language: ', padx=20)
        lang_label.grid(row=0, sticky="e")
        default_lang = StringVar(self.top_frame)
        default_lang.set(self.languages[0]) # default value
        self.lang_val = OptionMenu(self.top_frame, default_lang, "Php", "Python", command=self.langEvent)
        self.lang_val.configure(width=20)
        self.lang_val.grid(row=0, column=1, sticky="w")


        server_label = Label(self.top_frame, text='Web Server: ', padx=20)
        server_label.grid(row=2, sticky="e")
        self.default_server = StringVar(self.top_frame)
        self.default_server.set(self.frameworks[0]) # default value
        self.server_val = OptionMenu(self.top_frame, self.default_server, *self.frameworks)
        self.server_val.configure(width=20)
        self.server_val.grid(row=2, column=1, sticky="w")

        # lang_val = Entry(self.top_frame)
        # lang_val.grid(row=0, column=1)


        # width_label = Label(self.top_frame, text='Width:')
        # length_label = Label(self.top_frame, text='Length:')
        # entry_W = Entry(self.top_frame, background="pink")
        # entry_L = Entry(self.top_frame, background="orange")

        # layout the widgets in the top frame
        # width_label.grid(row=1, column=0)
        # length_label.grid(row=1, column=2)
        # entry_W.grid(row=1, column=1)
        # entry_L.grid(row=1, column=3)

        # create the center widgets
        self.center.grid_rowconfigure(0, weight=1)
        self.center.grid_columnconfigure(1, weight=1)

        ctr_left = Frame(self.center, bg='blue', width=100, height=190)
        ctr_mid = Frame(self.center, bg='yellow', width=250, height=190, padx=3, pady=3)
        ctr_right = Frame(self.center, bg='green', width=100, height=190, padx=3, pady=3)

        ctr_left.grid(row=0, column=0, sticky="ns")
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_right.grid(row=0, column=2, sticky="ns")

    def langEvent(self, event):
        self.default_server.set("")
        frmwrks = self.server_val["menu"]
        frmwrks.delete(0, "end")
        if event == "Php":
            self.frameworks = ["Laravel", "Core Php"]
        if event == "Python":
            self.frameworks = ["Django", "Flask", "Masonite"]
        for string in self.frameworks:
            frmwrks.add_command(label=string, command=lambda value=string: self.default_server.set(value))

    def __str__(self):
        return 'config'

    def destroy(self):
        self.frame.destroy()
        #self.footer.canvas.destroy()
