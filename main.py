from datetime import datetime
from fastapi import FastAPI
from detabase import PoemTable
from models import Poem
import random
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    res = PoemTable.put(poem.dict())
    return res

@app.get("/poems")
async def get_poems(page: int = 1):
    poems = PoemTable.fetch(query=[{"is_verified": True}])
    return poems.items

@app.get("/poems/{id}")
async def get_poem(id: str):
    poem = PoemTable.get(id)
    return poem
