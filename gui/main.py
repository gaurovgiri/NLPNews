from app import Application
from tkinter import *
from dotenv import dotenv_values


config = dotenv_values(".env")


if __name__ == "__main__":
    root = Tk()
    myapp = Application(root,config["API-TOKEN"])
    root.mainloop()
