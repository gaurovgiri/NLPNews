"""
Import NLPCloud
"""
import nlpcloud

class AO_NEWS:

    _categories = ["Entrepreneurs", "Astrology", "Physics","Software","Programming","Lifestyle","Entertainment","Politics"]
    
    
    _models = {"summarize": "bart-large-cnn",

              "classify": "bart-large-mnli-yahoo-answers"}

    def __init__(self, token):
        self.token = token

    # Summarizes the given text
    def summarize(self, text):
            client = nlpcloud.Client(self._models["summarize"], self.token)
            res = client.summarization(text, size="large")
            return res["summary_text"]
   

    # Classify through the given categories
    def classify(self, text):
            client = nlpcloud.Client(self._models["classify"], self.token)
            res = client.classification(text,self._categories,True)
            output = {}
            for label,score in zip(res["labels"],res["scores"]):
                output[label] = score
            return output


