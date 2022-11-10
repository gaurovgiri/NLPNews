from pydantic import BaseModel


class newsRequest(BaseModel):
    text:str
    # title, body, date....

class newsResponse(BaseModel):
    summary_text:str
    categories:dict
