"""Importing necessary modules"""
from dotenv import dotenv_values
from fastapi import FastAPI

from model import newsRequest, newsResponse
from ao_news import AO_NEWS

config = dotenv_values(".env")
news = AO_NEWS(config["API-TOKEN"])

app = FastAPI()


@app.get("/")
def root():
    """Returns Online Status"""
    return {"Anmup": "Online"}


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
