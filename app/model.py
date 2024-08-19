from pydantic import BaseModel

class VowelCountRequest(BaseModel):
    words: list[str]

class SortRequest(VowelCountRequest):
    order: str