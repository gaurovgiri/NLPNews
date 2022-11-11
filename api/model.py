from pydantic import BaseModel


class newsRequest(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": """Colorado Republican Rep. Lauren Boebert – who splashed onto the political scene in 2020 as a young Second Amendment evangelist and quickly cemented her image as a Trump-thumping MAGA Republican – is staring down what could be the biggest upset of the 2022 election cycle in a race that was considered locked in her favor. ‟The red wave has begun”, Boebert tweeted as polls began closing Tuesday evening. But as the sun rose over the Rockies on Wednesday morning, the firebrand conservative found herself underperforming in staggering fashion – one of several Republican candidates whose undecided races could cost her party control of both chambers."""
            }
        }
    # title, body, date....


class newsResponse(BaseModel):
    summary_text: str
    categories: dict
