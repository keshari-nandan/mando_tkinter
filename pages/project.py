from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from .base import Base
import tkinter as tk
import json
import validators
import os


class Project(Base):

    def __init__(self, app):
        super().__init__(app, "Projects")
        self.newWindow = None
        self.name_val = None
        self.vhost_val = None
        self.dir_val = None
        row, column = app.root.grid_size()
        # Add new Project Button
        new_project = Button(self.top_frame, text="Add Project", cursor="hand1", command=self.setupProject)
        new_project.grid(row=1,sticky="e", columnspan=column)

        # Draw horizontal line
        # canvas = Canvas(self.top_frame, height=1, bg = "gray")
        # canvas.create_line(15, 25, 200, 25)
        # canvas.grid(row=3, columnspan=column)

        projects = self.getProjects()
        if not projects:
            message = Label(self.top_frame, text="No Project Exist.", fg="green")
            message.config(width=50)
            message.grid(row=4, columnspan=column)
        else:
            next_row = 5
            project_count = 1
            for item in projects.values():
                prjct = LabelFrame(self.top_frame, padx=3, pady=3, text=item["name"])
                prjct.grid(row=next_row, sticky="ew")
                next_row += 1
                Label(prjct, text="Host: ", padx=10).grid(row=next_row, column=2, sticky="e")
                Label(prjct, text=item["vhost"]).grid(row=next_row, column=3, sticky="w")
                
                Label(prjct, text="Directory: ", padx=10).grid(row=next_row, column=5, sticky="e")
                Label(prjct, text=item["dir"]).grid(row=next_row, column=6, sticky="w")
                next_row += 1
                Button(prjct, text="Edit", bg="SkyBlue1", cursor="hand1", command=lambda name=item["name"]: self.editProject(name)).grid(row=next_row, column=5, sticky="e")
                Button(prjct, text="Delete", bg="IndianRed1", cursor="hand1", command=lambda name=item["name"]: self.deleteProject(name)).grid(row=next_row, column=6, sticky="e")

                next_row += 1
                project_count += 1

        # Bottom of page
        back_btn = Button(self.center, text="Configuration", fg="white", bg="RoyalBlue1", activebackground="RoyalBlue2",
                            relief="flat", width="12", cursor="hand1", command=self.previousPage)
        back_btn.grid(sticky="w")


    def editProject(self, project):
        self.setupProject(project=project)
        

    def deleteProject(self, project):
        projects = self.getProjects()
        if project in projects:
            del projects[project]
            self.storeProjects(projects)
        self.refresh()
        messagebox.showinfo("Success","Project [" + project + "] deleted successfully.", parent=self.top_frame)  

    def previousPage(self):
        self.app.switchWindow('config')


    def setupProject(self, project=None):
        window_text = "New Project"
        projects = self.getProjects()

        if project is None:
            data = {}
        elif project in projects:
            data = projects[project]
            window_text = "Edit - " + project
        else:
            messagebox.showerror("Error","Project [" + project + "] does not exist.", parent=self.top_frame)

        self.newWindow = tk.Toplevel()
        project = LabelFrame(self.newWindow, pady=3, text=window_text)
        bottom = Frame(self.newWindow, padx=3, pady=3)
        project.grid(row=0, sticky="ew")
        bottom.grid(row=7, sticky="e")

        #Project Name
        name_label = Label(project, text="Project Name: ", padx=20)
        name_label.grid(row=1, sticky="e")
        self.name_val = StringVar(project)
        name = Entry(project, width=30, textvariable=self.name_val)
        if "name" in data:
            self.name_val.set(data["name"])
        name.grid(row=1, column=1, sticky="w")

        #Virtual Host
        vhost_label = Label(project, text="Virtual Host: ", padx=20)
        vhost_label.grid(row=2, sticky="e")
        self.vhost_val = StringVar(project)
        vhost = Entry(project, width=30, textvariable=self.vhost_val)
        if "vhost" in data:
            self.vhost_val.set(data["vhost"])
        vhost.grid(row=2, column=1, sticky="w")

        #Project Path
        dir_label = Label(project, text="Project Directory: ", padx=20)
        dir_label.grid(row=3, sticky="e")
        self.dir_val = StringVar(project)
        dir = Entry(project, width=30, textvariable=self.dir_val)
        if "dir" in data:
            self.dir_val.set(data["dir"])
        dir.grid(row=3, column=1, sticky="w")

        submit_btn = Button(bottom, text="Submit", fg="white", bg="RoyalBlue1", activebackground="RoyalBlue2", relief="flat", width="8", command=self.submitProject)
        submit_btn.grid(row=7, column=3, sticky="e")

    def submitProject(self):
        if len(self.name_val.get()) <= 0:
            messagebox.showerror("Error","Please enter project name", parent=self.newWindow)  
        elif len(self.vhost_val.get()) <= 0:
            messagebox.showerror("Error","Please enter virtual host", parent=self.newWindow) 
        elif len(self.dir_val.get()) <= 0:
            messagebox.showerror("Error","Please enter project directory path", parent=self.newWindow) 
        elif not os.path.isdir(self.dir_val.get()):
            messagebox.showerror("Error","Invalid Project Directory: " + self.dir_val.get(), parent=self.newWindow)  
        else:
            data = {
                "name": self.name_val.get(),
                "vhost": self.vhost_val.get(),
                "dir": self.dir_val.get(),
            }
            projectName = self.getProjectName(self.name_val.get())
            projects = self.getProjects()
            projects[projectName] = data
            self.storeProjects(projects)
            self.newWindow.destroy()
            messagebox.showinfo("Success","Project [" + projectName + "] stored successfully.", parent=self.top_frame)
            self.refresh()


    def getProjectName(self, string):
        return ''.join(e for e in string if e.isalnum())


    def storeProjects(self, data):
        file_w = open("settings/projects.json", "w")
        json.dump(data, file_w)
        file_w.close()
    

    def getProjects(self):
        try:
            file_r = open("settings/projects.json", "r")
            projects = json.load(file_r)
            file_r.close()
        except Exception:
            projects = {}
        return projects

    def refresh(self):
        app = self.app
        self.destroy()
        self.__init__(app)