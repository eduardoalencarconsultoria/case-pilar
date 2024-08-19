from fastapi import FastAPI
from app.model import VowelCountRequest, SortRequest

app = FastAPI()


@app.post("/vowel_count")
async def vowel_count(vowel_count_request: VowelCountRequest):
    response = {}
    for word in vowel_count_request.words:
        response.update({word: _vowel_count(word)})
    return response


@app.post("/sort")
async def sort(sort_request: SortRequest):
    order = sort_request.order
    return sorted(sort_request.words, reverse=order == "desc")


def _vowel_count(word: str) -> int:
    count = 0
    vowel = set("aeiouAEIOU")

    for letter in word:
        if letter in vowel:
            count = count + 1

    return count
