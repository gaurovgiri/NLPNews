from tkinter import *
from tkinter import ttk

from ao_news import AO_NEWS

class Application:
      def __init__(self, root, token):
        self.news = AO_NEWS(token)
        self.root = root
        self.root.title("Anmup Online")
        self.root.geometry("1200x800+0+0")
        self.root.resizable(False, False)

       # summarizer

        heading = Label(self.root, font=("bold", 20), text="Summarize: ")
        heading.place(x=0, y=2)

        self.body = Text(self.root)
        self.body.place(x=100, y=30, height=400, width=1000)

        submit = Button(self.root, text="Submit",
                        bd='5', command=self.summarize)

        submit.place(x=200, y=450)

      def summarize(self):
        submitted_text = self.body.get("1.0", END)
        text = self.news.summarize(submitted_text)
        self.body.delete("1.0", END)
        self.body.insert(INSERT, text)

        copy = Button(self.root, text="Copy", bd=5, command=lambda: self.copyToClip(self.body.get("1.0",END)))
        copy.place(x=600,y=450)

      def copyToClip(self,text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text) 
