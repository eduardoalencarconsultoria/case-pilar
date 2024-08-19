from enum import Enum
from pydantic import BaseModel

class VowelCountRequest(BaseModel):
    words: list[str]

class OrderEnum(str, Enum):
    asc = 'asc'
    desc = 'desc'

class SortRequest(VowelCountRequest):
    order: OrderEnum