from datetime import datetime
from fastapi import FastAPI
from detabase import PoemTable
from models import Poem
import random

app = FastAPI()

@app.get("/")
async def root():
    """ Get a random poem from the database """
    poems = PoemTable.fetch(query=[{"is_verified": True}])
    count = poems.count
    lucky = random.randint(0, count-1)
    poem = poems.items[lucky]
    return poem

@app.post("/", response_model=Poem)
async def post(poem: Poem):
    res = PoemTable.put(poem)
    return res

@app.get("/poems")
async def get_poems(page: int = 1):
    poems = PoemTable.fetch(query=[{"is_verified": True}])
    return poems.items
