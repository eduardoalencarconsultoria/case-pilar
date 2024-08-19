from fastapi import FastAPI
from app.model import VowelCountRequest

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/vowel_count")
async def vowel_count(vowel_count_request: VowelCountRequest):
    response = {}
    for word in vowel_count_request.words:
        response.update({word: _vowel_count(word)})
    return response
    
def _vowel_count(word: str) -> int:
    count = 0
    vowel = set("aeiouAEIOU")

    for letter in word:
        if letter in vowel:
            count = count + 1

    return count
