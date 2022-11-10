from fastapi import FastAPI
from  news.ao_news import AO_NEWS 
from api.model import newsRequest, newsResponse
from dotenv import dotenv_values


config = dotenv_values(".env")
news = AO_NEWS(config["API-TOKEN"])

app = FastAPI()


@app.get("/")
def root():
    return {"Anmup": "Online"}



@app.post("/news/",response_model=newsResponse)
def news_post(req: newsRequest):
    res = {
        "summary_text": news.summarize(req.text),
        "categories": news.classify(req.text)
    }
    return res