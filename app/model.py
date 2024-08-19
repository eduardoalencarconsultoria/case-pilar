from pydantic import BaseModel

class VowelCountRequest(BaseModel):
    words: list