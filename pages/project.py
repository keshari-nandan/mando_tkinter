from tkinter import *
from tkinter import filedialog
from .base import Base
import json


class Project(Base):
    def __init__(self, app):
        super().__init__(app, "Project Setup")
        self.newWindow = None
        self.name_val = None
        self.vhost_val = None
        self.dir_val = None
        row, column = app.root.grid_size()
        # Add new Project Button
        new_project = Button(self.top_frame, text="Add Project", command=self.setupProject)
        new_project.grid(row=1,sticky="e", columnspan=column)

        canvas = Canvas(self.top_frame, height=1, bg = "gray")
        canvas.create_line(15, 25, 200, 25)
        canvas.grid(row=3, columnspan=column)

        if not self.projectExist():
            message = Message(self.top_frame, text="No Project", fg="green")
            message.config(width=100)
            message.grid(row=4, columnspan=column)


    def projectExist(self):
        return False


    def setupProject(self):
        self.newWindow = Toplevel()
        project = LabelFrame(self.newWindow, pady=3, text="New Project")
        bottom = Frame(self.newWindow, padx=3, pady=3)
        project.grid(row=0, sticky="ew")
        bottom.grid(row=7, sticky="e")

        #Project Name
        name_label = Label(project, text="Project Name: ", padx=20)
        name_label.grid(row=1, sticky="e")
        self.name_val = StringVar(project)
        name = Entry(project, width=30, textvariable=self.name_val)
        name.grid(row=1, column=1, sticky="w")

        #Virtual Host
        vhost_label = Label(project, text="Virtual Host: ", padx=20)
        vhost_label.grid(row=2, sticky="e")
        self.vhost_val = StringVar(project)
        vhost = Entry(project, width=30, textvariable=self.vhost_val)
        vhost.grid(row=2, column=1, sticky="w")

        #Project Path
        dir_label = Label(project, text="Project Directory: ", padx=20)
        dir_label.grid(row=3, sticky="e")
        self.dir_val = StringVar(project)
        dir = Entry(project, width=30, textvariable=self.dir_val)
        dir.grid(row=3, column=1, sticky="w")

        submit_btn = Button(bottom, text="Submit", fg="white", bg="RoyalBlue1", activebackground="RoyalBlue2", relief="flat", width="8", command=self.submitProject)
        submit_btn.grid(row=7, column=3, sticky="e")


    def submitProject(self):
        data = {
            "name": self.name_val.get(),
            "vhost": self.vhost_val.get(),
            "dir": self.dir_val.get(),
        }
        projectName = self.getProjectName(self.name_val.get())
        projects = {}
        try:
            file_r = open("settings/projects.json", "r")
            projects = json.load(file_r)
            file_r.close()
        except Exception:
            pass

        file_w = open("settings/projects.json", "w")
        projects[projectName] = data
        json.dump(projects, file_w)
        file_w.close()
        self.newWindow.destroy()




    def getProjectName(self, string):
        return ''.join(e for e in string if e.isalnum())
