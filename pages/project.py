from tkinter import *
from .footer import Footer
from .base import Base


class Project(Base):
    def __init__(self, app):
        super().__init__(app, "Project Setup")
