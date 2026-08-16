from enum import Enum
from pydantic import BaseModel, Field

class Language(str, Enum):
    EN = "en"
    AZ = "az"
    RU = "ru"

class PredictRequest(BaseModel):
    text: str = Field(min_length=1, max_length=500)
    language: Language




request = PredictRequest(
    text="Hello AI",
    language="en"
)
print("------------------------------------")
print(request)
print(type(request.language))    
print("------------------------------------")
try:
    PredictRequest(text="Hi AI",
        language="frech")
except Exception as e:
    print(e)
try:
    PredictRequest(text="Hi AI",
        language=45)
except Exception as e:
    print(e)    