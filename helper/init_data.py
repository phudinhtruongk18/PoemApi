import json
from DATABASE import PoemTable


with open("poems.json", "r", encoding="utf-8") as f:
    poems = json.load(f)

for poem in poems:
    PoemTable.put(poem)
