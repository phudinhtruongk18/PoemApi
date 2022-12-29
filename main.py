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

@app.post("/add/", response_model=Poem)
async def post(poem: Poem):
    res = PoemTable.put(poem.dict())
    return res
