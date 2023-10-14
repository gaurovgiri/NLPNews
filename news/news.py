import nlpcloud


class News:
    """
    A class for summarizing and classifying news articles using NLP models.
    """

    _categories = [
        "Health",
        "Technology",
        "News",
        "Entertainment",
        "Sports",
        "Education",
        "Fashion",
        "Politics",
        "Travel",
        "Science"
    ]

    _models = {
        "summarize": "bart-large-cnn",
        "classify": "bart-large-mnli-yahoo-answers",
        "headline": "t5-base-en-generate-headline"
    }

    def __init__(self, token):
        self.token = token

    def summarize(self, text):
        """
        Summarizes the given text using the BART-Large-CNN model.

        Args:
            text (str): The text to be summarized.

        Returns:
            str: The summarized text.
        """
        client = nlpcloud.Client(self._models["summarize"], self.token)
        res = client.summarization(text, size="large")
        return res["summary_text"]

    def headline(self, text):
        client = nlpcloud.Client(self._models["headline"], self.token)
        res = client.summarization(text)
        return res["summary_text"]

    def classify(self, text):
        """
        Classifies the given text into one of the pre-defined categories.

        Args:
            text (str): The text to be classified.

        Returns:
            dict: A dictionary containing the classification labels and their corresponding scores.
        """
        client = nlpcloud.Client(self._models["classify"], self.token)
        res = client.classification(text, self._categories, True)
        output = dict(zip(res["labels"], res["scores"]))
        return output
