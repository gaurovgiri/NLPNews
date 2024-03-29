from tkinter import *
from tkinter import ttk

from news.news import News

class Application:
    """
    A graphical user interface (GUI) application for summarizing and categorizing news articles using NLP models.

    Attributes:
        root (Tk): The root Tkinter window.
        token (str): The API token for accessing NLPCloud services.
        news (News): An instance of the News class for text processing.
    """

    def __init__(self, root, token):
        """
        Initializes the Application.

        Args:
            root (Tk): The root Tkinter window.
            token (str): The API token for accessing NLPCloud services.
        """
        self.news = News(token)
        self.root = root
        self.root.title("News NLP")
        self.root.geometry("1200x800+0+0")
        self.root.resizable(False, False)

        # Summarizer
        self.heading = Label(self.root, font=("bold", 20), text="Summarize: ")
        self.heading.place(x=500, y=2)

        self.body = Text(self.root)
        self.body.place(x=100, y=35, height=400, width=1000)

        # Submit button
        submit = Button(self.root, text="Submit", bd='5', command=self.run)
        submit.place(x=200, y=450)

    def run(self):
        """
        Runs the summarization and categorization process when the "Submit" button is clicked.
        """

        # Headline
        self.heading.config(text=self.news.headline(self.body.get("1.0", END)))

        # Summarize
        submitted_text = self.body.get("1.0", END)
        text = self.news.summarize(submitted_text.strip())
        self.body.delete("1.0", END)
        self.body.insert(INSERT, text)


        # Categorize
        categories = self.news.classify(text.strip())
        suggested = Label(self.root, font=("bold", 10), text="Suggested Categories:")
        suggested.place(x=450, y=500)

        categories_list = Listbox(self.root)
        categories_list.place(x=450, y=550, height=200, width=300)

        threshold = 0.5
        index = 1
        for label, score in categories.items():
            if score > threshold:
                categories_list.insert(index, label)
                index += 1

        # Copy button
        copy = Button(self.root, text="Copy", bd=5, command=lambda: self.copyToClip(self.body.get("1.0", END)))
        copy.place(x=800, y=450)

    def copyToClip(self, text):
        """
        Copies the provided text to the clipboard.

        Args:
            text (str): The text to be copied to the clipboard.
        """
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
