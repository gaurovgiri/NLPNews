# NLP News :

NLP News is a tool for summarizing and categorizing a news. It uses NLPcloud and fastapi. You can check [NLP Cloud](https://nlpcloud.com) for more info about them.


## SETUP:

- $`git clone https://github.com/gaurovgiri/NLPNews`
- $`cd NLPNews`
- $`pip install -r requirements.txt` 
- Rename `.env.example` to `.env`
- Put your API-TOKEN generated from [NLP Cloud](https://nlpcloud.com) in `.env`


## How to run:
$`python run.py api` for api
$`python run.py gui` for gui

### API:
- $`uvicorn api.main:app --reload`
- Open `127.0.0.1:8000/docs` in browser to check for the api documentation.

### GUI:
    - $`python3 -m gui`