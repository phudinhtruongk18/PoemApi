import json
from detabase import PoemTable


with open("data/poems.json", "r", encoding="utf-8") as f:
    poems = json.load(f)

for poem in poems:
    poem["is_verified"] = True
    PoemTable.put(poem)
