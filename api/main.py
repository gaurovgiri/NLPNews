"""Importing necessary modules"""
from dotenv import dotenv_values
from fastapi import FastAPI

from api.model import newsRequest, newsResponse
from news.news import News

config = dotenv_values(".env")
news = News(config["API-TOKEN"])

app = FastAPI()


@app.get("/")
def root():
    """Returns Online Status"""
    return {"I am": "Online"}


@app.post("/news/", response_model=newsResponse)
def news_post(req: newsRequest):
    """
    Returns the summarized and categories scores
    """

    res = {
        "summary_text": news.summarize(req.text),
        "categories": news.classify(req.text)
    }
    return res
