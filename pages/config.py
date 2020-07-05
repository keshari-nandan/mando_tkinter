from tkinter import *
from .footer import Footer
from .base import Base
import json


class Config(Base):
    def __init__(self, app):
        self.languages = ['Php', 'Python']
        self.frameworks = ["Laravel", "Core Php"]
        self.servers = ['Nginx', 'Apache']
        self.versions = ["7.4", "7.3", "7.2", "7.1", "7.0"]
        self.databases = ["MySQL", "MariaDB", "PostgreSQL", "MongoDB"]
        super().__init__(app, "Configuration")

        # Programming Language Selection
        lang_label = Label(self.top_frame, text='Programming Language: ', padx=20)
        lang_label.grid(row=0, sticky="e")
        self.default_lang = StringVar(self.top_frame)
        self.default_lang.set(self.languages[0])  # default value
        self.lang_val = OptionMenu(self.top_frame, self.default_lang, *self.languages, command=self.langEvent)
        self.lang_val.configure(width=10)
        self.lang_val.grid(row=0, column=1, sticky="w")

        # Programming Language versions Selection
        self.default_version = StringVar(self.top_frame)
        self.default_version.set(self.versions[0])  # default value
        self.version_val = OptionMenu(self.top_frame, self.default_version, *self.versions)
        self.version_val.configure(width=10)
        self.version_val.grid(row=0, column=3, sticky="w")

        # Framework Selection
        framework_label = Label(self.top_frame, text='Framework: ', padx=20)
        framework_label.grid(row=2, sticky="e")
        self.default_framework = StringVar(self.top_frame)
        self.default_framework.set(self.frameworks[0])  # default value
        self.framework_val = OptionMenu(self.top_frame, self.default_framework, *self.frameworks)
        self.framework_val.configure(width=10)
        self.framework_val.grid(row=2, column=1, sticky="w")

        # Web Server Selection
        server_label = Label(self.top_frame, text='Web Server: ', padx=20)
        server_label.grid(row=3, sticky="e")
        self.default_server = StringVar(self.top_frame)
        self.default_server.set(self.servers[0])  # default value
        self.server_val = OptionMenu(self.top_frame, self.default_server, *self.servers)
        self.server_val.configure(width=10)
        self.server_val.grid(row=3, column=1, sticky="w")

        # Databse Selection
        db_label = Label(self.top_frame, text='Database : ', padx=20)
        db_label.grid(row=4, sticky="e")
        self.default_db = StringVar(self.top_frame)
        self.default_db.set(self.databases[0])  # default value
        self.db_val = OptionMenu(self.top_frame, self.default_db, *self.databases)
        self.db_val.configure(width=10)
        self.db_val.grid(row=4, column=1, sticky="w")

        # Redis Configuration
        redis_label = Label(self.top_frame, text='Redis: ', padx=20)
        redis_label.grid(row=5, sticky="e")
        self.redis_val = BooleanVar(self.top_frame)
        self.redis_val.set(False)
        self.redis_opt = Checkbutton(self.top_frame, var=self.redis_val)
        self.redis_opt.grid(row=5, column=1, sticky="w")

        # Message Broker
        broker_label = Label(self.top_frame, text='Message Broker: ', padx=20)
        broker_label.grid(row=6, sticky="e")
        self.activemq_val = BooleanVar(self.top_frame)
        self.activemq_val.set(False)
        self.activemq_opt = Checkbutton(self.top_frame, text="ActiveMQ", var=self.activemq_val)
        self.activemq_opt.grid(row=6, column=1, sticky="w")
        self.rabbitmq_val = BooleanVar(self.top_frame)
        self.rabbitmq_val.set(False)
        self.rabbitmq_opt = Checkbutton(self.top_frame, text="RabbitMQ", var=self.rabbitmq_val)
        self.rabbitmq_opt.grid(row=6, column=3, sticky="w")

        # Submit Buttom
        submit_btn = Button(self.center, text="Next", fg="white", bg="RoyalBlue1", activebackground="RoyalBlue2",
                            relief="flat", width="8", command=self.nextClicked)
        submit_btn.grid(row=7, column=3, sticky="e")

    def nextClicked(self):
        config = {
            "language": self.default_lang.get(),
            "lang_version": self.default_version.get(),
            "framework": self.default_framework.get(),
            "server": self.default_server.get(),
            "database": self.default_db.get(),
            "redis": self.redis_val.get(),
            "activemq": self.activemq_val.get(),
            "rabbitmq": self.rabbitmq_val.get()
        }
        file = open('settings/system.json', 'w')
        json.dump(config, file)
        file.close()
        self.app.switchWindow('project')


    def langEvent(self, event):
        self.setFramework(event)
        self.setVersion(event)
        self.setServer(event)

    def setFramework(self, event):
        self.frameworks = []
        self.default_framework.set("")
        items = self.framework_val["menu"]
        items.delete(0, "end")
        if event == "Php":
            self.frameworks = ["Laravel", "Core Php"]
        if event == "Python":
            self.frameworks = ["Django", "Flask", "Masonite"]
        for item in self.frameworks:
            items.add_command(label=item, command=lambda value=item: self.default_framework.set(value))
        self.default_framework.set(self.frameworks[0])

    def setVersion(self, event):
        self.versions = []
        self.default_version.set("")
        items = self.version_val["menu"]
        items.delete(0, "end")
        if event == "Php":
            self.versions = ["7.4", "7.3", "7.2", "7.1", "7.0"]
        if event == "Python":
            self.versions = ["3.8", "3.7", "3.6"]
        for item in self.versions:
            items.add_command(label=item, command=lambda value=item: self.default_version.set(value))
        self.default_version.set(self.versions[0])

    def setServer(self, event):
        self.servers = []
        self.default_server.set("")
        items = self.server_val["menu"]
        items.delete(0, "end")
        if event == "Php":
            self.servers = ['Nginx', 'Apache']
        if event == "Python":
            self.servers = ['Apache']
        for item in self.servers:
            items.add_command(label=item, command=lambda value=item: self.default_server.set(value))
        self.default_server.set(self.servers[0])

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
        # self.center.grid_rowconfigure(0, weight=1)
        # self.center.grid_columnconfigure(1, weight=1)
        #
        # ctr_left = Frame(self.center, bg='blue', width=100, height=190)
        # ctr_mid = Frame(self.center, bg='yellow', width=250, height=190, padx=3, pady=3)
        # ctr_right = Frame(self.center, bg='green', width=100, height=190, padx=3, pady=3)
        #
        # ctr_left.grid(row=0, column=0, sticky="ns")
        # ctr_mid.grid(row=0, column=1, sticky="nsew")
        # ctr_right.grid(row=0, column=2, sticky="ns")
